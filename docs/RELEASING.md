# Releasing and repository settings

## One-time GitHub settings (owner only; the assistant cannot set these)
**Visibility:** the repository is public. Several settings below (code scanning, secret scanning with push protection, rulesets) depend on that; on a private repository they depend on the GitHub plan.

Repository → **Settings**:
1. **General** → Description: "Agent skills for evaluating, planning and stress-testing ideas (Claude, Copilot, ChatGPT)" Topics: `agent-skills`, `claude-skills`, `skill-md`, `idea-validation`, `prioritization`, `product-management`, `github-copilot`, `chatgpt`. (Add an `adhd` topic only once user feedback supports the claim.) Features: enable Issues; Discussions optional; disable Wiki and Projects if unused. Enable **Automatically delete head branches**.
2. **Code security** → enable: *Private vulnerability reporting* (SECURITY.md relies on it), *Dependency graph*, *Dependabot alerts* and *security updates*, *Secret scanning* and *Push protection*, *Code scanning* (the CodeQL workflow uploads results).
3. **Branches** → add a rule for `main`: require a pull request before merging, require status checks (`checks (3.10)`, `checks (3.12)`, `analyze`), require branches to be up to date, block force pushes and deletions. For a solo maintainer keep "Do not allow bypassing" off if you want to merge your own PRs; require at least 0 or 1 approvals as you prefer.
4. **Actions → General**: workflow permissions "Read repository contents" (workflows request more only where needed); disable "Allow GitHub Actions to create and approve pull requests" unless wanted.
5. **Rules** → add a tag ruleset for `v*` so only maintainers can create release tags. The release workflow additionally refuses tags that are not semantic versions or not on `main`, and refuses a CHANGELOG heading still marked "(unreleased)".
6. **Labels**: `bug` and `enhancement` exist by default; create `feedback` (used by the feedback issue form) under Issues → Labels.
7. **Pages / Sponsors**: not used.

Actions are pinned to major versions (`checkout@v7`, `setup-python@v7`, `codeql-action@v4`, `upload-artifact@v7`, `download-artifact@v8`, checked 2026-10-02); Dependabot proposes updates weekly. Pinning to commit SHAs is stronger and recommended once the workflows have run green.

## Release checklist
1. Branch is merged into `main` and CI is green.
2. `CHANGELOG.md`: section `## X.Y.Z[-beta.N]` is final (replace "(unreleased)" with the date `YYYY-MM-DD`); known limits still accurate.
3. `python tests/run_all.py` passes locally; `dist/*.skill` rebuilt and committed (`python tools/build_packages.py`).
4. Skim `SKILL.md` diffs for accidental personal data or invented facts.
5. **Do not create the release or the tag by hand.** Go to Actions → **Release** → Run workflow (branch `main`) and type the version without `v`, for example `3.1.0-beta.2`.
6. The workflow verifies the changelog section, runs all checks and creates a **draft** release with `*.skill` and `SHA256SUMS` attached (a pre-release if the version contains `-`).
7. Open Releases, check the draft (four `.skill` files, checksums, notes), then press **Publish release**; this creates the tag. Releases are immutable once published: files cannot be added later and the tag name cannot be reused. Install one package in a clean client to smoke-test.
8. Announce only after step 7. Say plainly that it is a beta with the known limits listed.

## Version policy
Suite releases use semantic versions of the repository. Individual skills carry their own version in the `SKILL.md` title. Breaking changes to the Idea Card format bump the suite's major version.

## Moving from beta to stable (criteria)
Trigger accuracy of the three descriptions measured in a real client; head-to-head on the same ideas with at least one comparable tool, judged blind; feedback from real users (including users with ADHD) collected through the feedback issue template; weights and thresholds re-checked on real cases.
