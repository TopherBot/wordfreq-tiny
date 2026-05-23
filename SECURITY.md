# Security Policy

## Reporting a Vulnerability
If you discover a security issue, please **do not** open a public issue. Instead, email us at `security@your‑domain.example` with details. We will acknowledge receipt within 48 hours and aim to resolve the issue promptly.

## Automated Scanning
- GitHub secret scanning is enabled.
- Pull‑request workflows run TruffleHog (see `.github/workflows/ci.yml`).
- CodeQL runs on every push to the default branch.

## Dependency Security
We use Dependabot (enabled in repository settings) to receive automated alerts and PRs for vulnerable dependencies.

## Token Permissions
All GitHub Actions workflows request the minimal `read` permissions. No workflow writes back to the repository unless explicitly granted.

---
*This repository follows the 2024 GitHub security checklist: least‑privilege permissions, pinned actions, secret scanning, and CODEOWNERS protection (see CODEOWNERS file).*