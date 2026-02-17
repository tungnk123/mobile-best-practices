import { existsSync, mkdirSync, cpSync, readFileSync, writeFileSync, symlinkSync, lstatSync, unlinkSync, rmSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { homedir } from 'os';
import type { PlatformConfig, MobilePlatform } from '../types/index.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const CACHE_DIR = join(homedir(), '.mobile-best-practices');

export function getAssetsDir(): string {
  return join(__dirname, '..', '..', 'assets');
}

export function getTemplatesDir(): string {
  return join(getAssetsDir(), 'templates');
}

export function getCacheDir(): string {
  return CACHE_DIR;
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

/**
 * Install assets to the central cache (~/.mobile-best-practices/)
 * and generate the SKILL.md with paths pointing to the cache.
 */
export function installToCache(mobilePlatform: MobilePlatform = 'all'): void {
  const assetsDir = getAssetsDir();
  const cacheDir = getCacheDir();

  // Copy data, scripts, references to cache
  copyDir(join(assetsDir, 'data'), join(cacheDir, 'data'));
  copyDir(join(assetsDir, 'scripts'), join(cacheDir, 'scripts'));
  copyDir(join(assetsDir, 'references'), join(cacheDir, 'references'));

  // Generate SKILL.md in cache with ~/.mobile-best-practices as the skill path
  const skillsDir = join(assetsDir, 'skills');
  const skillFileName = mobilePlatform === 'all' ? 'all.md' : `${mobilePlatform}.md`;
  const platformSkillPath = join(skillsDir, skillFileName);

  let content: string;
  if (existsSync(platformSkillPath)) {
    content = readFileSync(platformSkillPath, 'utf-8');
    content = content.replace(/\{SKILL_PATH\}/g, '~/.mobile-best-practices');
  } else {
    const baseContent = readFileSync(
      join(getTemplatesDir(), 'base', 'skill-content.md'),
      'utf-8'
    );
    const quickRef = readFileSync(
      join(getTemplatesDir(), 'base', 'quick-reference.md'),
      'utf-8'
    );

    let processedBase = baseContent.replace(/\{SKILL_PATH\}/g, '~/.mobile-best-practices');
    let processedQuickRef = quickRef.replace(/\{SKILL_PATH\}/g, '~/.mobile-best-practices');

    content = `---
name: mobile-best-practices
description: "Mobile development intelligence for Android, iOS, Flutter, and React Native. 2,024 best practices."
---

${processedBase}

${processedQuickRef}
`;
  }

  writeFileSync(join(cacheDir, 'SKILL.md'), content, 'utf-8');
}

/**
 * Create a symlink, removing any existing file/symlink/directory at the link path.
 */
function createSymlink(target: string, linkPath: string): void {
  ensureDir(dirname(linkPath));

  // Remove existing file/symlink/directory at link path
  try {
    const stat = lstatSync(linkPath);
    if (stat.isSymbolicLink() || stat.isFile()) {
      unlinkSync(linkPath);
    } else if (stat.isDirectory()) {
      rmSync(linkPath, { recursive: true });
    }
  } catch {
    // Does not exist, that's fine
  }

  symlinkSync(target, linkPath, 'dir');
}

export function generateSkillFile(
  config: PlatformConfig,
  targetDir: string,
  mobilePlatform: MobilePlatform = 'all'
): void {
  const assetsDir = getAssetsDir();
  const skillsDir = join(assetsDir, 'skills');

  // Always use ~/.mobile-best-practices as the skill path for search commands
  const skillPath = '~/.mobile-best-practices';

  // Try to load platform-specific skill file
  const skillFileName = mobilePlatform === 'all' ? 'all.md' : `${mobilePlatform}.md`;
  const platformSkillPath = join(skillsDir, skillFileName);

  let content: string;

  if (existsSync(platformSkillPath)) {
    content = readFileSync(platformSkillPath, 'utf-8');
    content = content.replace(/\{SKILL_PATH\}/g, skillPath);
  } else {
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
description: "Mobile development intelligence for Android, iOS, Flutter, and React Native. 2,024 best practices."
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
  const cacheDir = getCacheDir();

  // Install assets to central cache (~/.mobile-best-practices/)
  installToCache(mobilePlatform);

  if (config.type === 'skill' || config.type === 'skills') {
    // Create a single symlink: e.g. .claude/skills/mobile-best-practices → ~/.mobile-best-practices/
    const targetDir = join(projectDir, config.installPath);
    createSymlink(cacheDir, targetDir);
  } else {
    // For rules/instructions/workflow, generate the platform-specific file only
    // No need to copy data/scripts - the rule file references ~/.mobile-best-practices/ directly
    const targetDir = join(projectDir, config.installPath);
    generateSkillFile(config, targetDir, mobilePlatform);
  }

  // Copy slash commands for Claude, Cursor, and OpenCode (OUTSIDE the skill-type block)
  if (platform === 'claude' || platform === 'cursor' || platform === 'opencode') {
    const commandsDir = join(getAssetsDir(), 'commands');
    if (existsSync(commandsDir)) {
      const targetCommandsDir = platform === 'claude'
        ? join(projectDir, '.claude', 'commands')
        : platform === 'cursor'
          ? join(projectDir, '.cursor', 'commands')
          : join(projectDir, '.opencode', 'commands');
      copyDir(commandsDir, targetCommandsDir);
    }
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
    patterns.push('OPENCODE.md');
  }
  if (platform === 'copilot' || platform === 'all') {
    patterns.push('.github/copilot-instructions.md');
  }
  if (platform === 'codex' || platform === 'all') {
    patterns.push('AGENTS.md');
  }
  if (platform === 'gemini' || platform === 'all') {
    patterns.push('GEMINI.md');
  }
  if (platform === 'agent' || platform === 'all') {
    patterns.push('AGENT.md');
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
