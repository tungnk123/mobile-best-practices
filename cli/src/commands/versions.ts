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
