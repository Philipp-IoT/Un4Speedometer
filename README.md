# UN4 Speedometer Workspace

## Virtual environment workflow

1. Ensure you have Python 3.10+ installed locally.
2. From the project root, run the helper script via:
   ```bash
   source scripts/manage_venv.sh
   ```
   - The script creates `.venv` if it doesn't exist, upgrades `pip`, installs `requirements.txt`, and leaves the shell activated.
   - Because it is sourced, the activation persists in your current terminal session. Use `deactivate` to exit the environment.
3. When using VS Code, the workspace already points to `.venv/bin/python` via `.vscode/settings.json`, so new terminals open inside the IDE will auto-activate the environment.

## Manual alternative

If you prefer not to source the script, you can run the familiar commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Either approach keeps dependencies pinned to `requirements.txt` and plays nicely with MkDocs commands such as `mkdocs serve`.

## MkDocs build script

To render the documentation into `site/`, run:

```bash
./scripts/build_docs.sh
```

- The script auto-detects `mkdocs` from your active shell or the local `.venv`.
- Output is written to `site/`, which is ignored by git but ready for inspection or publishing.
- Pass additional MkDocs flags as needed, for example `./scripts/build_docs.sh --clean`.

### Live preview server

For a hot-reloading preview that watches your docs, run:

```bash
./scripts/serve_docs.sh
```

- Defaults to `127.0.0.1:8000`; override with `DEV_ADDR=0.0.0.0:8080 ./scripts/serve_docs.sh`.
- MkDocs' built-in `watch:` config (in `mkdocs.yml`) already keeps the full `docs/` tree—including `notes/`—under live-reload without custom scripting.
- Auto-reload relies on the `watchdog` package (now part of `requirements.txt`). After pulling updates, rerun `source scripts/manage_venv.sh` so the dependency is installed; confirm via `pip show watchdog` if reload still misbehaves.
- Accepts any MkDocs `serve` flags (e.g., `--dirtyreload`).
- Stop the server with `Ctrl+C` or by terminating the VS Code task described below.

Both helpers are exposed as VS Code tasks (`docs: build` and `docs: serve`) so you can trigger them via the Command Palette ("Run Task") without touching the terminal.

### Adding new notes pages

- Drop Markdown files anywhere under `docs/notes/` (e.g., `docs/notes/new_sensor.md`).
- Navigation updates automatically via `mkdocs-awesome-pages-plugin`, so no manual `nav:` edits are required.
- Re-run `./scripts/build_docs.sh` or `./scripts/serve_docs.sh` to pick up the changes.
- (Optional) Create a `.pages` file inside the folder if you want to override ordering or titles for that subtree.

## Continuous integration & deployment

- Every push to the `main` (and legacy `master`) branch, plus manual dispatches, trigger the `deploy-docs` GitHub Actions workflow located in `.github/workflows/docs-build.yml`.
- The workflow installs dependencies from `requirements.txt`, runs `mkdocs build --strict` using the repository-root `mkdocs.yml`, uploads the generated `site/` directory as a Pages artifact, and deploys it via `actions/deploy-pages`.
- The published site is served from GitHub Pages under the repository’s Pages URL (visible in the workflow summary). Inspect the Actions tab for logs, artifacts, and the live URL after each deployment.
