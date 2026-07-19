"""
Generates a retro-terminal GIF for the GitHub profile README using the
`github-readme-terminal` package (https://github.com/x0rzavi/github-readme-terminal).

Run locally to test:
    pip install github-readme-terminal
    python generate_terminal.py
Produces: output.gif

In CI (see .github/workflows/terminal.yml), GITHUB_TOKEN is provided
automatically by GitHub Actions, so fetch_github_stats() works without
any extra secrets.
"""

import gifos

t = gifos.Terminal(width=800, height=420, xpad=12, ypad=12)

# --- Boot / whoami ---
t.gen_text(text="jiphin@github:~$ whoami", row_num=1)
t.gen_text(text="\x1b[35mJiphin George\x1b[0m", row_num=2)
t.gen_text(text="", row_num=3)

# --- About ---
t.gen_text(text="jiphin@github:~$ cat about.txt", row_num=4)
t.gen_text(text="AI/ML Engineer | Full Stack Developer", row_num=5)
t.gen_text(text="MCA Student @ Mar Athanasius College of Engineering", row_num=6)
t.gen_text(text="", row_num=7)

# --- Tech stack ---
t.gen_text(text="jiphin@github:~$ cat stack.txt", row_num=8)
t.gen_text(text="Python | Java | JS | Flutter | Django | Flask | React", row_num=9)
t.gen_text(text="TensorFlow | Keras | OpenCV | Scikit-learn", row_num=10)
t.gen_text(text="", row_num=11)

# --- Live GitHub stats ---
# NOTE: fetch_github_stats() has a known bug — it divides by the merged
# PR count internally, which throws ZeroDivisionError for accounts with
# no merged PRs yet. Skipping it until that's fixed upstream.
t.gen_text(text="jiphin@github:~$ neofetch --github", row_num=12)
t.gen_text(text="GitHub: JiphinGeorge", row_num=13)
t.gen_text(text="Status: Open to Software Engineer / AI-ML roles", row_num=14)

t.gen_gif()
