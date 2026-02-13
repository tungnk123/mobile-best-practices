import { existsSync, mkdirSync, cpSync, readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import type { PlatformConfig, MobilePlatform } from '../types/index.js';

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
  targetDir: string,
  mobilePlatform: MobilePlatform = 'all'
): void {
  const assetsDir = getAssetsDir();
  const skillsDir = join(assetsDir, 'skills');
  const skillPath = config.skillPath;

  // Try to load platform-specific skill file
  const skillFileName = mobilePlatform === 'all' ? 'all.md' : `${mobilePlatform}.md`;
  const platformSkillPath = join(skillsDir, skillFileName);

  let content: string;

  if (existsSync(platformSkillPath)) {
    // Use platform-specific SKILL.md
    content = readFileSync(platformSkillPath, 'utf-8');
    content = content.replace(/\{SKILL_PATH\}/g, skillPath);
  } else {
    // Fallback to template-based generation
    const baseContent = readFileSync(
      join(getTemplatesDir(), 'base', 'skill-content.md'),
      'utf-8'
    );
    const quickRef = readFileSync(
      join(getTemplatesDir(), 'base', 'quick-reference.md'),
      'utf-8'
    );

    let processedBase = baseContent.replace(/\{SKILL_PATH\}/g, skillPath);
    let processedQuickRef = quickRef.replace(/\{SKILL_PATH\}/g, skillPath);

    content = `---
name: mobile-best-practices
description: "Mobile development intelligence for Android, iOS, Flutter, and React Native. 1,738 best practices."
---

${processedBase}

${processedQuickRef}
`;
  }

  const targetFile = join(targetDir, config.files.skill || config.files.rule || config.files.instructions || config.files.workflow || 'SKILL.md');
  ensureDir(dirname(targetFile));
  writeFileSync(targetFile, content, 'utf-8');
}

export function installForPlatform(
  platform: string,
  projectDir: string,
  mobilePlatform: MobilePlatform = 'all'
): void {
  const config = loadPlatformConfig(platform);
  const targetDir = join(projectDir, config.installPath);

  ensureDir(targetDir);

  // Copy data and scripts
  const assetsDir = getAssetsDir();
  if (config.type === 'skill' || config.type === 'skills') {
    copyDir(join(assetsDir, 'data'), join(targetDir, 'data'));
    copyDir(join(assetsDir, 'scripts'), join(targetDir, 'scripts'));
    copyDir(join(assetsDir, 'references'), join(targetDir, 'references'));
    generateSkillFile(config, targetDir, mobilePlatform);

    // Copy custom slash commands for Claude Code and Cursor
    if (platform === 'claude' || platform === 'cursor') {
      const commandsDir = join(assetsDir, 'commands');
      if (existsSync(commandsDir)) {
        const targetCommandsDir = platform === 'claude'
          ? join(projectDir, '.claude', 'commands')
          : join(projectDir, '.cursor', 'commands');
        copyDir(commandsDir, targetCommandsDir);
      }
    }
  } else {
    // For rules/instructions/workflow, generate a single file
    generateSkillFile(config, targetDir, mobilePlatform);
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

export function updateGitignore(projectDir: string, platform: string): void {
  const gitignorePath = join(projectDir, '.gitignore');

  // Patterns to add based on platform
  const patterns: string[] = [];

  if (platform === 'claude' || platform === 'all') {
    patterns.push('.claude/');
  }
  if (platform === 'cursor' || platform === 'all') {
    patterns.push('.cursor/');
  }
  if (platform === 'windsurf' || platform === 'all') {
    patterns.push('.windsurf/');
  }
  if (platform === 'opencode' || platform === 'all') {
    patterns.push('.opencode/');
  }
  if (platform === 'copilot' || platform === 'all') {
    patterns.push('.github/copilot/');
  }
  if (platform === 'roocode' || platform === 'all') {
    patterns.push('.roo/');
  }
  if (platform === 'continue' || platform === 'all') {
    patterns.push('.continue/');
  }
  if (platform === 'kiro' || platform === 'all') {
    patterns.push('.kiro/');
  }
  if (platform === 'qoder' || platform === 'all') {
    patterns.push('.qoder/');
  }
  if (platform === 'codebuddy' || platform === 'all') {
    patterns.push('.codebuddy/');
  }
  if (platform === 'trae' || platform === 'all') {
    patterns.push('.trae/');
  }
  if (platform === 'antigravity' || platform === 'all') {
    patterns.push('.antigravity/');
  }

  // Also add shared directory
  patterns.push('.mobile-best-practices/');

  let content = '';
  if (existsSync(gitignorePath)) {
    content = readFileSync(gitignorePath, 'utf-8');
  }

  // Add header comment if not present
  const header = '# AI Assistant Skills (mobile-best-practices)';
  let needsUpdate = false;

  if (!content.includes(header)) {
    content += (content && !content.endsWith('\n\n') ? '\n\n' : '') + header + '\n';
    needsUpdate = true;
  }

  // Add missing patterns
  for (const pattern of patterns) {
    if (!content.includes(pattern)) {
      content += pattern + '\n';
      needsUpdate = true;
    }
  }

  if (needsUpdate) {
    writeFileSync(gitignorePath, content, 'utf-8');
  }
}
