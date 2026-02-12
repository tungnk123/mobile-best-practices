import chalk from 'chalk';
import ora from 'ora';

export async function updateCommand(): Promise<void> {
  const spinner = ora('Checking for updates...').start();

  try {
    // Check npm for latest version
    const response = await fetch('https://registry.npmjs.org/mobilepro-cli/latest');

    if (!response.ok) {
      spinner.info('Package not yet published to npm. Run locally with: npm link');
      return;
    }

    const data = await response.json();
    const { version: localVersion } = await import('../../package.json', { with: { type: 'json' } });

    if (data.version === localVersion) {
      spinner.succeed(`Already on latest version: ${chalk.green(localVersion)}`);
    } else {
      spinner.info(`Update available: ${chalk.yellow(localVersion)} -> ${chalk.green(data.version)}`);
      console.log();
      console.log(chalk.dim('  Run to update:'));
      console.log(chalk.white('  npm install -g mobilepro-cli@latest'));
    }
  } catch {
    spinner.warn('Could not check for updates. Using local version.');
  }
}
