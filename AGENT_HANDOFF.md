# Agent Handoff: Istofi Yusuf GitHub Profile README

## Current Goal

The user wants a polished GitHub profile README for `istofiyusuf` that presents Istofi Yusuf as a **Fullstack Developer & AI Engineer**. The profile should be fully English, professional, and strong enough to showcase his builder work in web development, AI automation, design engineering, and DevOps.

## User Preferences

- Language: full English.
- Positioning: **Fullstack Developer & AI Engineer**.
- Visual direction: clean premium "Developer Builder", not noisy cyber/hacker style.
- Contact links for v1: GitHub only for now.
- README strategy: hybrid.
  - Curated story, featured projects, focus areas, and tech stack are manual.
  - Recent public GitHub activity is auto-updated inside a bounded generated block.

## Implemented Repository

Local path:

```text
/home/yusuf/Desktop/NextJS Project/istofiyusuf
Remote repo:

text
https://github.com/istofiyusuf/istofiyusuf
The repo was created as a public GitHub special profile repository.

Default branch:

text
main
Implemented Files
text
istofiyusuf/
├── README.md
├── AGENT_HANDOFF.md
├── assets/
│   ├── header.png
│   ├── header.svg
│   ├── profile.webp
│   └── hero/
│       ├── agent-console-v5-dark.svg
│       ├── agent-console-v5-light.svg
│       ├── agent-console-v5-mobile-dark.svg
│       └── agent-console-v5-mobile-light.svg
├── data/
│   └── featured-projects.json
├── docs/
│   └── agent-hero.md
├── scripts/
│   ├── generate-agent-hero.mjs
│   └── update-readme.mjs
└── .github/
    └── workflows/
        └── update-readme.yml
README Content Summary
The current README includes:

Header image with animated SVG (dark/light theme support)

GitHub badge CTA

About Me

Current Focus table

Featured Work table (6 projects)

Tech Stack badges (6 categories: Frontend, Backend, AI, Design, Social, DevOps)

Recent Activity generated block

The current positioning copy is:

text
I am Istofi Yusuf, a versatile developer and creator from Indonesia with expertise spanning fullstack development, AI automation, UI/UX design, and DevOps.
Featured Projects
The README highlights exactly these projects:

Active Projects
ZENMOVIE

Repo: https://github.com/istofiyusuf/zenmovie

Positioning: Full-stack anime & donghua streaming platform with multi-server support.

ShopVerse

Repo: https://github.com/istofiyusuf/shopverse

Positioning: Fullstack e-commerce marketplace with multi-payment gateway integration.

Zenverse

Repo: https://github.com/istofiyusuf/zenverse

Positioning: Android APK distribution platform with categorized downloads.

Upcoming Projects
AI Flow Studio

Repo: https://github.com/istofiyusuf/ai-flow-studio

Positioning: No-code AI automation platform with visual flow builder.

Pixel Forge

Repo: https://github.com/istofiyusuf/pixel-forge

Positioning: Browser-based design tool with AI capabilities.

DevHub Dashboard

Repo: https://github.com/istofiyusuf/devhub-dashboard

Positioning: All-in-one developer dashboard for project management.

Automation Details
Script:

text
scripts/update-readme.mjs
Purpose:

Fetches recent public GitHub events for istofiyusuf.

Converts selected event types into readable markdown bullets.

Replaces only the bounded README block:

md
<!-- AUTO:ACTIVITY:START -->
...
<!-- AUTO:ACTIVITY:END -->
Supported event types:

PushEvent

CreateEvent

PullRequestEvent

IssuesEvent

Commands to test:

bash
node scripts/update-readme.mjs --dry-run
node scripts/update-readme.mjs
Workflow:

text
.github/workflows/update-readme.yml
Workflow name:

text
Update profile README
Schedule:

text
17 1 * * *
Also supports manual workflow_dispatch.

Tech Stack Categories
The README showcases 6 skill categories with 50+ badges:

Category	Skills
Frontend	React, Next.js, TypeScript, Three.js, Tailwind CSS, Vue.js, HTML5, CSS3, JavaScript
Backend	Node.js, Express, Python, FastAPI, PostgreSQL, MongoDB, GraphQL, REST API
AI & Automation	OpenAI, LangChain, Chatbot, Prompt Engineering, Zapier, Make
Design	Figma, UI/UX, Web Design, Mobile Design, Prototyping, Design Systems, Video Editing, Motion Graphics, 3D Modeling, Audio Production
Social & Marketing	Content Creation, Social Media Strategy, Instagram/TikTok, YouTube, SEO, Adobe Premiere, Copywriting, Brand Strategy
DevOps & Tools	Docker, AWS, Vercel, CI/CD, Git, GitHub, Linux, Nginx, Kubernetes, Terraform, GitHub Actions, Monitoring
Portrait Hero System
The profile hero is an animated SVG console with:

Desktop: 1180x610 layout

Mobile: 720x1080 stacked layout

Dark & light theme variants

Portrait image placed at assets/profile.webp

System information panel with identity, research, builds, and links

Useful Commands
Check local status:

bash
cd ~/Desktop/NextJS\ Project/istofiyusuf
git status --short --branch
Run README activity update:

bash
node scripts/update-readme.mjs --dry-run
node scripts/update-readme.mjs
Generate hero assets (requires ffmpeg):

bash
node scripts/generate-agent-hero.mjs --source /path/to/portrait.webp
Check remote:

bash
gh repo view istofiyusuf/istofiyusuf --json nameWithOwner,visibility,isFork,isEmpty,defaultBranchRef,url
Check raw README:

bash
curl -s https://raw.githubusercontent.com/istofiyusuf/istofiyusuf/main/README.md | sed -n '1,120p'
Style Guidance for Future Edits
Keep the README:

English-only

concise and professional

builder-credible

focused on fullstack development, AI automation, and design engineering

not overloaded with stats or decorative animations

Avoid turning it into:

a generic "hire me" profile

a noisy badge wall

a raw auto-generated repo dashboard

a casual biography without technical positioning

text

---