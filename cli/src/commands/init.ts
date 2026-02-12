import chalk from 'chalk';
import ora from 'ora';
import prompts from 'prompts';
import { SUPPORTED_PLATFORMS, type AIPlatform, type MobilePlatform } from '../types/index.js';
import { installForPlatform } from '../utils/index.js';

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

  console.log();
  console.log(chalk.green('Mobile Best Practices skill installed successfully!'));
  console.log(chalk.dim(`Platform: ${mobilePlatform}`));
  console.log();
  console.log(chalk.dim('Usage:'));
  if (aiPlatform === 'claude' || aiPlatform === 'all') {
    console.log(chalk.dim('  Just chat naturally with Claude Code:'));
    if (mobilePlatform === 'android') {
      console.log(chalk.white('  "Build a product list screen with Compose"'));
    } else if (mobilePlatform === 'ios') {
      console.log(chalk.white('  "Build a settings screen with SwiftUI"'));
    } else if (mobilePlatform === 'flutter') {
      console.log(chalk.white('  "Build a product list with BLoC"'));
    } else if (mobilePlatform === 'react-native') {
      console.log(chalk.white('  "Build a product list with React Navigation"'));
    } else {
      console.log(chalk.white('  "Build a product list screen for my e-commerce app"'));
    }
  }
  console.log();
}
