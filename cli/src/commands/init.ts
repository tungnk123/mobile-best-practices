import chalk from 'chalk';
import ora from 'ora';
import prompts from 'prompts';
import { SUPPORTED_PLATFORMS, type AIPlatform, type MobilePlatform } from '../types/index.js';
import { installForPlatform, updateGitignore } from '../utils/index.js';

export async function initCommand(options: { ai?: string; offline?: boolean; platform?: string }): Promise<void> {
  let aiPlatform = options.ai as AIPlatform;
  let mobilePlatform = options.platform as MobilePlatform | undefined;

  if (!aiPlatform) {
    const response = await prompts({
      type: 'select',
      name: 'platform',
      message: 'Which AI assistant are you using?',
      choices: [
        { title: 'Claude Code', value: 'claude' },
        { title: 'Cursor', value: 'cursor' },
        { title: 'Windsurf', value: 'windsurf' },
        { title: 'GitHub Copilot', value: 'copilot' },
        { title: 'Kiro', value: 'kiro' },
        { title: 'Codex CLI', value: 'codex' },
        { title: 'Gemini CLI', value: 'gemini' },
        { title: 'Roo Code', value: 'roocode' },
        { title: 'Continue', value: 'continue' },
        { title: 'OpenCode', value: 'opencode' },
        { title: 'Qoder', value: 'qoder' },
        { title: 'CodeBuddy', value: 'codebuddy' },
        { title: 'Trae', value: 'trae' },
        { title: 'Antigravity', value: 'antigravity' },
        { title: 'All assistants', value: 'all' },
      ],
    });

    if (!response.platform) {
      console.log(chalk.yellow('Installation cancelled.'));
      return;
    }
    aiPlatform = response.platform;
  }

  if (!mobilePlatform) {
    const response = await prompts({
      type: 'select',
      name: 'mobilePlatform',
      message: 'Which mobile platform are you building for?',
      choices: [
        { title: 'Android (Jetpack Compose)', value: 'android' },
        { title: 'Android (XML Views)', value: 'android-xml' },
        { title: 'iOS (SwiftUI)', value: 'ios' },
        { title: 'Flutter (Dart)', value: 'flutter' },
        { title: 'React Native (TypeScript)', value: 'react-native' },
        { title: 'All platforms', value: 'all' },
      ],
    });

    if (!response.mobilePlatform) {
      console.log(chalk.yellow('Installation cancelled.'));
      return;
    }
    mobilePlatform = response.mobilePlatform;
  }

  const projectDir = process.cwd();
  const aiPlatforms = aiPlatform === 'all' ? SUPPORTED_PLATFORMS : [aiPlatform];

  for (const p of aiPlatforms) {
    const spinner = ora(`Installing for ${chalk.cyan(p)} (${chalk.dim(mobilePlatform)})...`).start();
    try {
      installForPlatform(p, projectDir, mobilePlatform);
      spinner.succeed(`Installed for ${chalk.green(p)} (${mobilePlatform})`);
    } catch (error) {
      spinner.fail(`Failed for ${chalk.red(p)}: ${(error as Error).message}`);
    }
  }

  // Update .gitignore to exclude AI assistant directories
  try {
    updateGitignore(projectDir, aiPlatform);
  } catch (error) {
    // Non-critical error, just log it
    console.log(chalk.yellow(`Note: Could not update .gitignore: ${(error as Error).message}`));
  }

  console.log();
  console.log(chalk.green('✓ Mobile Best Practices skill installed successfully!'));
  console.log(chalk.dim(`  Platform: ${mobilePlatform}`));
  console.log(chalk.dim(`  Cache: ~/.mobile-best-practices/`));
  console.log(chalk.dim(`  Mode: symlink (no files copied into project)`));
  console.log();

  console.log(chalk.cyan('How to use:'));
  console.log(chalk.dim('  No commands needed - just chat naturally with your AI assistant!'));
  console.log(chalk.dim('  The AI will automatically search 2,024 best practices as you work.'));
  console.log();

  console.log(chalk.yellow('Examples:'));
  if (mobilePlatform === 'android' || mobilePlatform === 'all') {
    console.log(chalk.white('  • "Review my project for security issues"'));
    console.log(chalk.white('  • "Build a login screen with Compose"'));
    console.log(chalk.white('  • "Check my code for performance problems"'));
  } else if (mobilePlatform === 'android-xml') {
    console.log(chalk.white('  • "Review my XML layouts for performance"'));
    console.log(chalk.white('  • "Convert this Fragment to ViewBinding"'));
    console.log(chalk.white('  • "Check for memory leaks in my Activity"'));
  } else if (mobilePlatform === 'ios') {
    console.log(chalk.white('  • "Review my iOS app for security vulnerabilities"'));
    console.log(chalk.white('  • "Build a settings screen with SwiftUI"'));
    console.log(chalk.white('  • "Check my app for accessibility issues"'));
  } else if (mobilePlatform === 'flutter') {
    console.log(chalk.white('  • "Audit my Flutter app for OWASP issues"'));
    console.log(chalk.white('  • "Build a product list with BLoC"'));
    console.log(chalk.white('  • "Find performance bottlenecks in my app"'));
  } else if (mobilePlatform === 'react-native') {
    console.log(chalk.white('  • "Review my React Native app for anti-patterns"'));
    console.log(chalk.white('  • "Build a product list with React Navigation"'));
    console.log(chalk.white('  • "Optimize my FlatList performance"'));
  }
  console.log();
  console.log(chalk.dim('Tip: The skill works invisibly - no slash commands, no special syntax!'));

  // Add slash command info for Claude Code, Cursor and OpenCode
  if (aiPlatform === 'claude' || aiPlatform === 'cursor' || aiPlatform === 'opencode' || aiPlatform === 'all') {
    console.log();
    console.log(chalk.cyan('Slash commands (Claude Code, Cursor & OpenCode):'));
    console.log(chalk.dim('  Type / to see available commands:'));
    console.log(chalk.white('  • /mobile-best-practices - Main skill'));
    console.log(chalk.white('  • /mobile-security-audit - Security vulnerability scan'));
    console.log(chalk.white('  • /mobile-performance-check - Performance analysis'));
    console.log(chalk.white('  • /mobile-setup-android - New Android project setup'));
  }
  console.log();
}
