import chalk from 'chalk';
import type { Version } from '../types/index.js';

const VERSIONS: Version[] = [
  {
    version: '1.0.0',
    date: '2026-02-12',
    changes: [
      'Initial release',
      '1,738 mobile best practices across 15 CSV files',
      'Support for 15 AI coding assistants',
      'BM25 search engine with auto-domain detection',
      '--stack and --persist flags',
      '79 copy-paste code snippets (Android, iOS, Flutter, React Native)',
      '78 Gradle dependency declarations',
      '49 architecture patterns',
      '415 platform-specific guidelines (Android 246, iOS 60, Flutter 54, React Native 55)',
      'Reference URLs for all entries',
    ],
  },
  {
    version: '1.1.1',
    date: '2026-02-13',
    changes: [
      'Fix: Automatically add OPENCODE.md to .gitignore',
      'Feat: Enable slash commands for OpenCode',
    ],
  },
  {
    version: '1.2.0',
    date: '2026-02-13',
    changes: [
      'Feat: Symlink install — assets cached at ~/.mobile-best-practices/, single symlink per project',
      'Fix: Slash commands now install for Cursor and OpenCode (were only installed for Claude)',
      'Fix: all.md uses {SKILL_PATH} instead of hardcoded Claude paths',
    ],
  },
  {
    version: '1.3.0',
    date: '2026-02-14',
    changes: [
      'Feat: Integration of Android Security Best Practices',
      'Feat: Enhanced Code Quality guidelines (Performance, Anti-patterns)',
      'Feat: Android XML View support',
      'Fix: Gitignore auto-update for AI assistant directories',
    ],
  },
  {
    version: '1.4.0',
    date: '2026-02-17',
    changes: [
      'Feat: Added more design pattern best practices',
      'Feat: Added Apollo Kotlin and Koin Annotations libraries',
      'Feat: New Android best practices for architecture, DI, networking, and testing',
    ],
  },
  {
    version: '1.4.1',
    date: '2026-02-17',
    changes: [
      'Feat: Migrate from Moshi to Kotlin Serialization',
      'Fix: Version bump for npm publish',
    ],
  },
  {
    version: '1.4.2',
    date: '2026-02-17',
    changes: [
      'Feat: Version compatibility matrix for AGP, Kotlin, KSP, Room, Hilt, Compose',
      'Feat: Anti-patterns for mismatched dependency versions',
      'Feat: Updated Compose BOM, Room, Hilt to latest stable versions',
      'Fix: Gitignore missing entries for Codex, Gemini, Agent, Copilot platforms',
    ],
  },
  {
    version: '1.4.3',
    date: '2026-02-17',
    changes: [
      'Fix: Enforce stringResource(R.string.xxx) for all user-visible text — no more hardcoded strings',
      'Fix: Remaining Moshi references in skill files and CODE-RULES.md replaced with Kotlin Serialization',
    ],
  },
];

export function versionsCommand(): void {
  console.log(chalk.bold('\nMobile Best Practices - Version History\n'));

  for (const v of VERSIONS) {
    console.log(`  ${chalk.green(v.version)} ${chalk.dim(`(${v.date})`)}`);
    for (const change of v.changes) {
      console.log(`    ${chalk.dim('-')} ${change}`);
    }
    console.log();
  }
}
