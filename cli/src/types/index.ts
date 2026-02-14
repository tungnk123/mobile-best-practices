export interface PlatformConfig {
  name: string;
  displayName: string;
  type: 'skill' | 'rules' | 'instructions' | 'workflow' | 'skills';
  installPath: string;
  files: Record<string, string>;
  settings?: {
    file: string;
    permissions: string[];
  };
  ruleFormat?: string;
  skillPath: string;
}

export type AIPlatform =
  | 'claude'
  | 'cursor'
  | 'windsurf'
  | 'copilot'
  | 'kiro'
  | 'codex'
  | 'gemini'
  | 'roocode'
  | 'continue'
  | 'opencode'
  | 'qoder'
  | 'codebuddy'
  | 'trae'
  | 'agent'
  | 'antigravity'
  | 'all';

export const SUPPORTED_PLATFORMS: AIPlatform[] = [
  'claude',
  'cursor',
  'windsurf',
  'copilot',
  'kiro',
  'codex',
  'gemini',
  'roocode',
  'continue',
  'opencode',
  'qoder',
  'codebuddy',
  'trae',
  'agent',
  'antigravity',
];

export type MobilePlatform = 'android' | 'android-xml' | 'ios' | 'flutter' | 'react-native' | 'all';

export const MOBILE_PLATFORMS: MobilePlatform[] = [
  'android',
  'ios',
  'flutter',
  'react-native',
];

export interface Version {
  version: string;
  date: string;
  changes: string[];
}
