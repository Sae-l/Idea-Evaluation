# Releasing and repository settings

## One-time GitHub settings (owner only; the assistant cannot set these)
Repository → **Settings**:
1. **General** → Description: "Three small, portable AI skills to evaluate ideas, plan them realistically and stress-test them. ADHD-friendly." Topics: `agent-skills`, `claude-skills`, `skill-md`, `idea-validation`, `prioritization`, `product-management`, `adhd`, `github-copilot`, `chatgpt`. Features: enable Issues; Discussions optional; disable Wiki and Projects if unused. Enable **Automatically delete head branches**.
2. **Code security** → enable: *Private vulnerability reporting* (SECURITY.md relies on it), *Dependency graph*, *Dependabot alerts* and *security updates*, *Secret scanning* and *Push protection*, *Code scanning* (the CodeQL workflow uploads results).
3. **Branches** → add a rule for `main`: require a pull request before merging, require status checks (`checks (3.10)`, `checks (3.12)`, `analyze`), require branches to be up to date, block force pushes and deletions. For a solo maintainer keep "Do not allow bypassing" off if you want to merge your own PRs; require at least 0 or 1 approvals as you prefer.
4. **Actions → General**: workflow permissions "Read repository contents" (workflows request more only where needed); disable "Allow GitHub Actions to create and approve pull requests" unless wanted.
5. **Tags** → add a tag protection/ruleset for `v*` so only maintainers can create release tags.
6. **Pages / Sponsors**: not used.

## Release checklist
1. Branch is merged into `main` and CI is green.
2. `CHANGELOG.md`: section `## X.Y.Z[-beta.N]` is final (replace "(unreleased)" with the date `YYYY-MM-DD`); known limits still accurate.
3. `python tests/run_all.py` passes locally; `dist/*.skill` rebuilt and committed (`python tools/build_packages.py`).
4. Skim `SKILL.md` diffs for accidental personal data or invented facts.
5. Tag and push: `git tag -a v3.1.0-beta.1 -m "v3.1.0-beta.1" && git push origin v3.1.0-beta.1`.
6. The **Release** workflow verifies the changelog section, runs all checks, attaches `*.skill` and `SHA256SUMS`, and publishes a GitHub release (a pre-release if the tag contains `-`).
7. Check the release page: three `.skill` files, checksums, notes. Install one in a clean client to smoke-test.
8. Announce only after step 7. Say plainly that it is a beta with the known limits listed.

## Version policy
Suite releases use semantic versions of the repository. Individual skills carry their own version in the `SKILL.md` title. Breaking changes to the Idea Card format bump the suite's major version.

## Moving from beta to stable (criteria)
Trigger accuracy of the three descriptions measured in a real client; head-to-head on the same ideas with at least one comparable tool, judged blind; feedback from real users (including users with ADHD) collected through the feedback issue template; weights and thresholds re-checked on real cases.
