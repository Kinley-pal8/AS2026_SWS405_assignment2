# Builds REPORT.md by re-running the report content from build_report.py with Markdown helpers.
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(HERE))
src = open(os.path.join(HERE, "build_report.py")).read()
body = src[src.index("# ------------------------------------------------------------------ 1 setup"):src.index("doc.save(OUT)")]

out = []
def w(s=""): out.append(s)

class Doc:
    def add_heading(self, text, level): w("#" * (level + 1) + " " + text); w()
doc = Doc()

def para(text="", bold=False, italic=False, size=None, align=None, after=None):
    if not text: return
    w(); w("**%s**" % text if bold else "*%s*" % text if italic else text); w()
def bullet(text, code=None): w("- " + text + ("`%s`" % code if code else ""))
def code(lines):
    w(); w("```text")
    for ln in lines:
        if "->" in ln and not ln.lstrip().startswith(("dead end", "DEAD END", "working", "note")):
            cmd, res = ln.split("->", 1)
            if cmd.strip(): w(cmd.rstrip())
            w("        → " + res.strip())
        else: w(ln)
    w("```"); w()
def table(headers, rows, widths):
    w(); w("| " + " | ".join(headers) + " |"); w("|" + "---|" * len(headers))
    for r in rows:
        w("| " + " | ".join("`%s`" % v if v.startswith(("flag{", "inctf{")) else v.replace("|", "\\|") for v in r) + " |")
    w()
def fig(lab, num, caption):
    w(); w("![Figure %s](screenshots/Lab%d/%s.png)" % (num, lab, num)); w()
    w("*Figure %s – %s*" % (num, caption)); w()
def flagbox(label, flag): w("> **%s** `%s`" % (label, flag)); w()
def pagebreak(): w("---"); w()

w("# SWS405 Digital Forensics – Assignment 2")
w("## MemLabs Memory Forensics Challenge – Labs 1 to 5"); w()
w("**Royal University of Bhutan · College of Science and Technology · Software Engineering Programme**"); w()
table(["", ""], [["**Student Name**", "[Your Name]"], ["**Student Number**", "[Your Student No.]"],
                 ["**Module Tutor**", "Pema Thinley"], ["**Semester**", "Autumn Semester 2026"],
                 ["**Submission Date**", "12 October 2026"], ["**Submission Type**", "Individual Assignment"]], None)
w("## Contents"); w()
for a, t in (("1-environment-and-setup", "1. Environment and Setup"), ("2-summary-of-flags", "2. Summary of Flags"),
             ("3-lab-1--beginners-luck", "3. Lab 1 – Beginner's Luck"), ("4-lab-2--a-new-world", "4. Lab 2 – A New World"),
             ("5-lab-3--the-evils-den", "5. Lab 3 – The Evil's Den"), ("6-lab-4--obsession", "6. Lab 4 – Obsession"),
             ("7-lab-5--black-tuesday", "7. Lab 5 – Black Tuesday"), ("8-conclusion", "8. Conclusion")):
    w("- [%s](#%s)" % (t, a))
w()
para("Note on screenshots: every figure is labelled \"Figure L.N\", where L is the lab number and N the step in that lab's "
     "investigation log. Commands in the logs are shown exactly as typed; long outputs were filtered with grep so the "
     "relevant lines are readable, and the unfiltered outputs are kept in the memlabs/out/ folder.", italic=True)
w("---"); w()

exec(body)

text = "\n".join(out)
text = re.sub(r"\n{3,}", "\n\n", text).replace("\n- ", "\n- ")
open(os.path.join(BASE, "REPORT.md"), "w").write(text.rstrip() + "\n")
print("saved REPORT.md")
