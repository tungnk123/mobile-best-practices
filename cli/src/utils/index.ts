import { existsSync, mkdirSync, cpSync, readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import type { PlatformConfig } from '../types/index.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export function getAssetsDir(): string {
  return join(__dirname, '..', '..', 'assets');
}

export function getTemplatesDir(): string {
  return join(getAssetsDir(), 'templates');
}

export function loadPlatformConfig(platform: string): PlatformConfig {
  const configPath = join(getTemplatesDir(), 'platforms', `${platform}.json`);
  if (!existsSync(configPath)) {
    throw new Error(`Platform config not found: ${platform}`);
  }
  return JSON.parse(readFileSync(configPath, 'utf-8'));
}

export function ensureDir(dir: string): void {
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }
}

export function copyDir(src: string, dest: string): void {
  ensureDir(dest);
  cpSync(src, dest, { recursive: true });
}

export function generateSkillFile(
  config: PlatformConfig,
  targetDir: string
): void {
  const baseContent = readFileSync(
    join(getTemplatesDir(), 'base', 'skill-content.md'),
    'utf-8'
  );
  const quickRef = readFileSync(
    join(getTemplatesDir(), 'base', 'quick-reference.md'),
    'utf-8'
  );

  const skillPath = config.skillPath;
  let content = baseContent.replace(/\{SKILL_PATH\}/g, skillPath);
  let quickRefContent = quickRef.replace(/\{SKILL_PATH\}/g, skillPath);

  const fullContent = `---
name: mobile-best-practices
description: "Mobile development intelligence for Android, iOS, Flutter, and React Native. 500+ best practices."
---

${content}

${quickRefContent}
`;

  const targetFile = join(targetDir, config.files.skill || config.files.rule || config.files.instructions || config.files.workflow || 'SKILL.md');
  ensureDir(dirname(targetFile));
  writeFileSync(targetFile, fullContent, 'utf-8');
}

export function installForPlatform(
  platform: string,
  projectDir: string
): void {
  const config = loadPlatformConfig(platform);
  const targetDir = join(projectDir, config.installPath);

  ensureDir(targetDir);

  // Copy data and scripts
  const assetsDir = getAssetsDir();
  if (config.type === 'skill' || config.type === 'skills') {
    copyDir(join(assetsDir, 'data'), join(targetDir, 'data'));
    copyDir(join(assetsDir, 'scripts'), join(targetDir, 'scripts'));
    generateSkillFile(config, targetDir);
  } else {
    // For rules/instructions/workflow, generate a single file
    generateSkillFile(config, targetDir);
    // Also copy data and scripts to a shared location
    const sharedDir = join(projectDir, '.mobile-best-practices');
    copyDir(join(assetsDir, 'data'), join(sharedDir, 'data'));
    copyDir(join(assetsDir, 'scripts'), join(sharedDir, 'scripts'));
  }

  // Create settings file if needed (Claude only)
  if (config.settings) {
    const settingsPath = join(projectDir, config.settings.file);
    ensureDir(dirname(settingsPath));

    let settings: any = {};
    if (existsSync(settingsPath)) {
      settings = JSON.parse(readFileSync(settingsPath, 'utf-8'));
    }

    if (!settings.permissions) {
      settings.permissions = { allow: [] };
    }
    if (!settings.permissions.allow) {
      settings.permissions.allow = [];
    }

    for (const perm of config.settings.permissions) {
      if (!settings.permissions.allow.includes(perm)) {
        settings.permissions.allow.push(perm);
      }
    }

    writeFileSync(settingsPath, JSON.stringify(settings, null, 2) + '\n', 'utf-8');
  }
}
