import chalk from 'chalk';
import ora from 'ora';
import prompts from 'prompts';
import { SUPPORTED_PLATFORMS, type AIPlatform } from '../types/index.js';
import { installForPlatform } from '../utils/index.js';

export async function initCommand(options: { ai?: string; offline?: boolean }): Promise<void> {
  let platform = options.ai as AIPlatform;

  if (!platform) {
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
    platform = response.platform;
  }

  const projectDir = process.cwd();
  const platforms = platform === 'all' ? SUPPORTED_PLATFORMS : [platform];

  for (const p of platforms) {
    const spinner = ora(`Installing for ${chalk.cyan(p)}...`).start();
    try {
      installForPlatform(p, projectDir);
      spinner.succeed(`Installed for ${chalk.green(p)}`);
    } catch (error) {
      spinner.fail(`Failed for ${chalk.red(p)}: ${(error as Error).message}`);
    }
  }

  console.log();
  console.log(chalk.green('Mobile Best Practices skill installed successfully!'));
  console.log();
  console.log(chalk.dim('Usage:'));
  if (platform === 'claude' || platform === 'all') {
    console.log(chalk.dim('  Just chat naturally with Claude Code:'));
    console.log(chalk.white('  "Build a product list screen for my e-commerce app"'));
  }
  console.log();
}
