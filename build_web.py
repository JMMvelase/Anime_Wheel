import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

spec = importlib.util.spec_from_file_location("anime_wheel", HERE / "anime_wheel.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

data = {
	"questions": [
		{
			"anime": q["anime"],
			"prompt": q["prompt"],
			"answer": q["answer"],
			"choices": list(q["choices"]),
			"kind": q["kind"],
			"symbol": q["symbol"],
			"colors": list(q["colors"]),
			"tier": q["tier"],
		}
		for q in module.QUESTIONS
	],
	"tiers": {k: {"name": v[0], "color": v[1], "pts": v[2]} for k, v in module.TIERS.items()},
	"teamColors": list(module.TEAM_COLORS),
	"defaultTeams": list(module.DEFAULT_TEAMS),
}

template = (HERE / "web" / "template.html").read_text(encoding="utf-8")
if "/*__DATA__*/ null" not in template:
	raise SystemExit("template placeholder missing")
html = template.replace("/*__DATA__*/ null", json.dumps(data, ensure_ascii=False))

out = HERE / "web" / "index.html"
out.write_text(html, encoding="utf-8")
print(f"wrote {out} ({len(data['questions'])} questions)")
