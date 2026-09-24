# Sales-Quoting — operating notes for Claude

**Keep this file current — update it whenever anything changes.**

---

## What this is

This repo is the working home for **Straw Hut Media's client-facing sales
documents**: proposals, quotes, and the long-form services agreements that
follow them. It is not an application. There is no build, no deploy, no tests.

The actual deliverables live in **Google Drive** (Docs) and are handed to
clients as **PDFs**. This repo holds the operating knowledge: house style,
pricing, document inventory, decisions already made, and what's still open.

Owner: **Ryan Tillotson**, Founder & CEO (`ryan@strawhutmedia.com`).

---

## HARD RULES — read before doing anything

1. **Never send email to a client, prospect, fan, or lead** without an
   explicit, same-turn instruction from Ryan to send it. Draft it and hand it
   back. This covers every tool — Gmail, SES, QuickBooks, anything.
2. **Email to Ryan himself is fine** without asking first. Only Ryan.
3. **Never share a Google Doc with anyone.** Every Doc listed below is
   private on purpose. Ryan shares things himself.
4. **Never trash a Google Doc that has been sent to a client.** See the
   incident under "What's broken" — this already went wrong once. Before
   trashing any Doc, check whether its link has gone out to anyone.
5. **Never quote the hourly studio rate** in a proposal. Retainer-first.
6. **Never say "AI"** in client-facing copy.
7. **The client always owns their show.** Straw Hut *runs* or *leads* it —
   never "owns" it. This wording matters and appears in every agreement.

---

## ⭐ HOUSE STYLE — the Die With Zero proposal is the standard (set 2026-09-23)

**Every client proposal is modelled on the DWZ proposal, Doc
`15d24sVuf9zk96bsEakHx71uk1j0OrYVRR1elmnYn500`.** Ryan wants new proposals
"as close to that as possible."

What the DWZ look actually is (measured from its export 2026-09-23. An
earlier note here said "plain Arial 11pt", which was **wrong**):
- Georgia serif for the 30pt title, italic subtitle, 16pt H1s and 11.5pt gold
  (`#8a6d3b`) H2s with a thin beige rule under each. Arial 10.5pt body text
  in `#1a1a1a`, single line spacing.
- Small gold all-caps kicker above the title. "Prepared for / by / Date" in
  9.5pt grey.
- En-dash (–) bullets.
- Tables: dark `#1a1a1a` header row with white bold text, cream `#f7f4ef`
  label cells, beige borders.
- Stacked `By: / Name: / Title: / Date:` signature blocks. A page footer that
  reads "<CLIENT> PODCAST · STRAW HUT MEDIA PROPOSAL · PAGE n".
- ⚠️ The DWZ footer address (822 N. Dillon St.) is stale. Use 7201 Melrose.

**How to reproduce it exactly: build from DWZ's own .docx, not from HTML.**
`tools/build_from_dwz.py` has the method: export DWZ as .docx
(`download_file_content`, docx MIME), deep-copy its paragraphs and tables as
prototypes, swap only the text, then upload the .docx with `create_file`
(it converts to a Google Doc). Verify by exporting the new Doc as HTML and
comparing fonts, sizes and colours against DWZ.

**Don't use an HTML upload for this.** Drive's HTML import was tested
2026-09-23 and it rounds every half-point size down (10.5 → 10), turns every
list into round bullets, turns paragraph rules into grey `<hr>` lines, and
ignores class-based bold. The .docx route keeps all of that.

**Why:** the Flying V proposal came to 1,125 words and 3 pages in a compact
style, but 1,182 words and 6 pages in the looser, oversized "designed"
style. Ryan read the 6-page one as "too long", so the styling makes the
difference, not the word count.

## How documents actually get produced

The Google Drive connector **cannot edit a Doc in place.** Every revision
means: create a brand-new Doc, then trash the old one (subject to rule 4).
Each new Doc gets a new ID and URL, so any link already sent goes stale.

The working pipeline for a **proposal** (see House Style above):

1. Export the DWZ proposal as .docx and run `tools/build_from_dwz.py`
   (edit its text blocks for the new client; it clones DWZ's own paragraphs,
   tables and footer, so the styling matches exactly).
2. Upload the .docx with `create_file` (base64, docx MIME). Drive converts
   it to a Google Doc.
3. **Verify**: export the new Doc as `text/html`, check fonts, sizes and
   colours against DWZ's export, render it with headless Chromium, and look
   at the pages (`pip install pypdfium2 pillow`). LibreOffice in the
   sandbox can't open these .docx files, so don't rely on it.
4. For a PDF, export the finished Google Doc as PDF so the two match.

`templates/docs-native.css` + `templates/proposal.html` are a plain Arial
fallback from before the DWZ style was measured. **Don't use them for
client proposals.**

### Formatting lessons Ryan has already given

- **Length is a real objection, and it's usually the styling.** See the
  1,125 vs 1,182 words (3 vs 6 pages) comparison above. Don't cut content he
  asked for. Strip the design first.
- When he says copy the structure of an existing proposal, mirror it
  section for section.
- Watch the literal `&amp;` bug: passing `&amp;` in a Drive file **title**
  renders literally. Set the title with plain `&` via `update_file` after
  creating.

---

## Pricing (source of truth: `strawhutmedia-site/src/views.js` → `PACKAGES`)

| Tier | Price/mo | Shape |
|---|---|---|
| Essential | **$2,450** | Client records; we edit, brand, distribute, publish |
| Premium (Studio) | **$4,350** | Adds studio recording, theme music, guest booking, dedicated manager |
| Ultimate (On-Location) | **$6,550** | Adds on-location shoot, 3–6 cameras, on-site producer |

Custom retainers exist outside this ladder (Die With Zero is $9,650/mo).

---

## Active clients

### Die With Zero — Pacaso, Inc. (Austin Allison, CEO & Co-Founder)

Custom engagement, not a package tier.

- **Retainer:** $9,650/month, from Oct 1, 2026
- **Initial Term:** Oct 1, 2026 → Mar 31, 2027 (6 months). Ryan deliberately
  cut this from the proposal's 12-month minimum.
- **After Mar 31, 2027:** converts automatically to month-to-month effective
  Apr 1, 2027, unless a new fixed term is signed first. 30-day termination.
- **Launch target:** Jan 1, 2027; biweekly cadence
- **Contacts:** `austin@pacaso.com`, `lauren@pacaso.com` (Austin's colleague)
- **Pass-through costs:** per-production-day budget (Studio Avenue $10,850 /
  Home Avenue $6,600) plus travel & accommodations, invoiced within 30 days
  of each shoot

**Status:** Ryan emailed the agreement to Austin and Lauren himself on
Mon Sep 21, 2026 (Gmail thread `1a0c0444b5ff92ce`). Awaiting their comments.

### Flying V Group (Robb Fahrion, Co-Founder & CEO)

Newport Beach performance digital-marketing agency, 450+ clients, founded
2016. Not a first-time podcaster — **skip Podcasting 101**, lead on
authority / credibility / pipeline. He is ROI- and attribution-driven and
was flagged as the strongest lead in his batch ($5k+/mo marketing budget).

- **Retainer:** $2,450/month (Essential), billed from Nov 1, 2026
- **Term:** 12-month minimum
- **Cadence:** up to 2 episodes/month. **No rollover of unused episodes —
  Ryan explicitly said not to include any rollover language at all.**
- **Format:** audio and video. Host is Robb.
- **Recording:** in-house at Flying V offices; they send us the media
- **Production begins** Nov 1, 2026; **launch** Jan 4, 2027
- **Transition (corrected by Ryan 2026-09-23):** Flying V *shoots* the first
  3 episodes, but Straw Hut *produces* them from the start. There's a lot of
  hands-on work helping them produce. Straw Hut never shoots on the in-house
  tier. The proposal's Startup & Transition section had this wrong; Ryan is
  pasting in the fix himself.
- **In-house tier scope:** original theme music IS included. No dedicated
  production manager and no shoot/guest scheduling (Flying V does both).
- **Payment:** card or ACH on file, charged at the top of each month
- **Studio upgrade** offered at $4,350/mo (Premium)
- **Show title:** TBD, to be developed together
- **Day-to-day contacts:** Robb and his team, names TBD

### If You Please — StardustBlue (Karen A. Brown) — added 2026-09-24

Show: **If You Please, Himan Brown's Radio Mystery Theater** (CUNY TV,
RSS `https://tv.cuny.edu/podcasts/ifyouplease.xml`) + the **Radio Drama
Network** YouTube channel (`@radiodramanetwork`). Karen (StardustBlue PR,
`stardustbluepr@gmail.com`) hires us through StardustBlue.

- **Growth only, no publishing:** landing page per episode + per-episode
  audience targeting for RSS downloads; matching YouTube growth for
  views/subscribers. We do NOT publish episodes or manage uploads.
- **$2,000/month total = $925 Straw Hut fee + $1,075 promotion budget.**
  Can increase if it works.
- **Geo:** primary focus on native-English countries (US, CA, UK, IE, AU,
  NZ), plus a worldwide test.
- **Term:** 6 months, Oct 1, 2026 → Mar 31, 2027. Card/ACH authorization
  form follows the signed proposal. **No long-form agreement: the proposal
  is the contract.**
- **No guarantees, by Ryan's instruction.** The proposal says plainly that
  it promises no specific download, view or subscriber numbers. Never add
  outcome promises to anything for this client.
- Proposal Doc (**current, 2 pages**, DWZ house style):
  `1H7kxceWFsOF5HFbHZMCsAAa2PO64Gw6jie5n3rhMtjo`, built with
  `tools/build_if_you_please.py`. The earlier 3-page version
  `1Jecf-Q2B-5LdxrTDDMAhHFzMs8fIQ2gM0n4YqRoPyx4` is superseded but **not
  trashed**, because Ryan had its link. Ask before trashing it.
- Karen's title on the signature block is left blank (unknown).
- Lesson: hand-copying a ~15KB base64 docx into `create_file` can fail with
  "invalid argument". Print it in 6,000-character chunks and copy each one
  exactly.

---

## Document inventory (Google Drive — all private, none shared)

| Document | File ID |
|---|---|
| DWZ — Podcast Services Agreement (current, has final Term language) | `1nGLsgfSD7LHs6k15aEKhN3qEem9nLq0XJM8YC5CVFvE` |
| DWZ — agreement version Ryan actually emailed to Pacaso | `1uKnKSW-XN400kzt2gf8jMgV-siaHxPeAbEQuojszM08` ⚠️ **in Drive trash — see below** |
| DWZ — original proposal (Sep 10, 2026) — **⭐ house-style standard for all proposals** | `15d24sVuf9zk96bsEakHx71uk1j0OrYVRR1elmnYn500` |
| Flying V Group — proposal (**current**, built from the DWZ docx 2026-09-23, in-house tier: theme music included, no production manager, no scheduling) | `1Gn7ya50DSoA9a8RG8C6tQX9pUswH3CK5vaFVVcq3cvk` |
| DWZ — brainstorm episode template + book outline (Ryan's original) | `1kl5_Rq7fW0HaKr26vwC4RwsKl6gQHGYMtOvkY047kpE` |

Superseded and **trashed**: both earlier Flying V proposal versions, including
`1iU457UVSsTSjUGIpV-Bj9f3CnOHACSDxTnd36Tq7eCc`. Don't reference them.

Superseded but **NOT trashed**. Ryan was sent these links on 2026-09-23 and
may have shared them, so ask before trashing:
`1piO8KDCilp1EX5rQwgUgJMV7aSBfowQSs2wnGu-9pdc` (Arial version),
`1-9dJFp8Uo0Ao1MTpHIHoOlMjnydO0Fgc4RuZH3rumSE` (HTML-import attempt),
`1PfVCbtwdY7xqGVAJ3y8llDt1nnPsNfIfuTd3NxRtrhY` (had the "absence of
episodes" sentence).

### Reference agreements — read these before drafting a new one

These are Straw Hut's real house style. Do not draft from generic
boilerplate.

| Comp | File ID | Why it matters |
|---|---|---|
| Justin Williams — Service Agreement (Feb 2026) | `1wyrykL-fSxZhWV1Qs5zJ0ssd4K7rLZ-FOz-IWCkatdk` | Primary template. Retainer-regardless-of-delays, work-for-hire, portfolio carve-out, mutual liability cap |
| CodeStrap — Service Agreement (Jan 2026) | `1MglHf1fMlNGV0KxeDVsNfE7n86zmCnSsN4L7S7u40_o` | Closest structural comp; validated the auto-charge payment clause |
| BGU Agreement_Redline (Jun 2026) | `10JOxvxzWHc0rKTwqNAtwnCTK01Lup_sEv3L9cF0oK5g` | Confirms California governing law is the house default |
| Universal / Seen on the Screen SOW | `1l7VY80fev4ZwBdzDrUqq9QdpXZcVeteH` | NBCU's paper, not ours — reference only |

---

## Key decisions and why

- **Insurance language is verified true.** Straw Hut carries commercial
  general liability **and** workers' compensation through **TCP Insurance /
  Great American Insurance Co.** Confirmed by reading actual policy-renewal
  emails in Gmail, because Ryan said: *"I don't want to say the workers comp
  bit if it isn't true."* Do not state coverage you have not re-verified.
- **Governing law is California.** BGU and Justin Williams both use it.
  CodeStrap's Delaware/Denver arbitration is a one-off outlier — don't copy it.
- **Guest-lawsuit liability sits with the client.** They own the show, direct
  the content, and control the channels. Folded into the Ownership section as
  a single paragraph, not a standalone indemnification block — Ryan said
  *"don't make a big deal out of this."*
- **Production day = 12 hours max, with a 30–60 minute break after every
  5 hours.** ⚠️ Ryan wrote "3-60 min break"; this was read as a typo for
  "30-60" and flagged to him, **but he never confirmed it.** Verify before
  this language goes into another agreement.
- **Notices and Assignment clauses were deliberately declined** for Die With
  Zero even though they appear in CodeStrap and BGU. Ryan: *"I don't think we
  need to worry about those last two."* Don't re-add them uninvited.
- **Straw Hut business address:** 7201 Melrose Ave., Suite 203, Los Angeles,
  CA 90046. The old DWZ proposal footer has 822 N. Dillon St. — that is
  **stale**, do not reuse it.

---

## Environment variables

**This repo has none** — no app, no build, no secrets. Work happens through
the Claude connectors (Google Drive, Gmail), which authenticate via OAuth,
not env vars.

Env var names for the *other* Straw Hut repos are documented in their own
`CLAUDE.md` files — `Project-management/CLAUDE.md` (Slate) and
`Podbooster/CLAUDE.md` are the detailed ones. Never put real keys in any
repo.

---

## What's broken / outstanding

1. **⚠️ HIGHEST PRIORITY — a live client link is dead.** Ryan emailed Austin
   and Lauren a link to Doc `1uKnKSW-XN400kzt2gf8jMgV-siaHxPeAbEQuojszM08`
   on Sep 21. A later session trashed that Doc during routine versioning,
   not knowing it had already been sent. **Their link is broken.** The Drive
   connector has no untrash operation, so **Ryan has to restore it manually**:
   Drive → Trash → "Straw Hut Media - Die With Zero - Podcast Services
   Agreement" → Restore. **Still not done as of 2026-09-23.** Ask him.
2. **The sent version is one revision behind.** Doc `1uKnKSW…` (what Pacaso
   has) predates the final Term-language tightening. The current text lives
   in `1nGLsgfSD7LHs6k15aEKhN3qEem9nLq0XJM8YC5CVFvE`. Decide with Ryan
   whether Pacaso needs the update or whether it rides along in redlines.
3. **The "3-60 min break" typo is still unconfirmed** (still open
   2026-09-23). See above.
4. **Flying V feed hosting is unanswered** (still open 2026-09-23). Asked who hosts the RSS and who
   pays (Megaphone on our account vs. theirs); the answer given — "he is the
   host" — was about Robb being the on-mic host. If hosting sits on Straw
   Hut's Megaphone account, that's a real monthly cost inside the $2,450 and
   the proposal doesn't mention it.
5. **Abandoned task:** reformatting the DWZ episode template. Two attempts
   (Docs `1OfXR5yh16OPspvTD3YwGpaXzXxppl6upkMYqob9M-wM` and
   `1gqAe39AjlFCQvCkZDjkokYGT2gT87GuwzK5mOBDJWsY`) were both rejected as too
   long, and Ryan called it off. Those two Docs are still sitting in Drive
   and can be trashed — he was offered and didn't answer. Don't restart this
   unless asked.

---

## Next steps

- [ ] Confirm Ryan restored the trashed DWZ agreement Doc from Drive trash
- [ ] Handle Pacaso's comments on the agreement when they come back
- [x] Restyle the Flying V proposal to DWZ house style (done 2026-09-23,
      Doc `1Gn7ya50DSoA9a8RG8C6tQX9pUswH3CK5vaFVVcq3cvk`)
- [ ] Ryan pastes the corrected "Startup & Transition" text (Straw Hut
      produces the first 3 episodes, Flying V shoots them) into that Doc.
      The Doc as built still has the old wording.
- [ ] Get the Flying V proposal in front of Robb (Ryan sends it, not Claude)
- [ ] Answer the Flying V feed-hosting question and amend if needed
- [ ] **Draft the Die With Zero renewal agreement** — effective Apr 1, 2027,
      to be presented around Mar 1, 2027, before the Mar 31 Initial Term
      expires. **Not started.** Reuse the current agreement's protective
      structure; term length not yet decided (12 months was the leaning).
- [ ] **Set a reminder for mid-to-late February 2027** to get that renewal
      moving. **Never set** — the tooling for it (`send_later` /
      `create_trigger`) is available but was not used.

---

## Context that's easy to lose

- There is a handoff email in Ryan's inbox, subject **"Die With Zero —
  Handoff / where things stand"**, sent Sep 21, 2026. It duplicates some of
  the above. This file supersedes it.
- The Google Docs are the source of truth for proposal text. The Flying V
  build script (with its text) is committed as `tools/build_from_dwz.py`.
- Git: this file first lived on `claude/tourism-podcast-pitch-olu47p` and
  `main` has only a README. The current working branch is
  `claude/sales-quoting-standards-wxbqx5`. Push with
  `git push -u origin <branch>`.
- **Merge your own PRs yourself — never wait on Ryan to merge.** Ryan,
  2026-09-23: *"You don't wait on me to merge, you merge!!"* Once a PR you
  opened is clean (no conflicts, no open review threads), mark it ready and
  merge it in the same session.
