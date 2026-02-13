#!/usr/bin/env node
import { Command } from 'commander';
import { initCommand } from './commands/init.js';
import { updateCommand } from './commands/update.js';
import { versionsCommand } from './commands/versions.js';

const program = new Command();

program
  .name('mobile-best-practices')
  .description('CLI to install Mobile Best Practices skill for AI coding assistants')
  .version('1.1.1');

program
  .command('init')
  .description('Install mobile best practices skill for your AI assistant')
  .option('--ai <platform>', 'AI assistant (claude, cursor, windsurf, copilot, kiro, codex, gemini, roocode, continue, opencode, qoder, codebuddy, trae, antigravity, all)')
  .option('--platform <mobile>', 'Mobile platform (android, ios, flutter, react-native, all)')
  .option('--offline', 'Skip GitHub, use bundled assets')
  .action(initCommand);

program
  .command('update')
  .description('Check for and install updates')
  .action(updateCommand);

program
  .command('versions')
  .description('List available versions and changelog')
  .action(versionsCommand);

program.parse();
