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
   back. This covers every tool — Gmail, Resend, QuickBooks, anything.
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

## How documents actually get produced

The Google Drive connector **cannot edit a Doc in place.** Every revision
means: create a brand-new Doc, then trash the old one (subject to rule 4).
Each new Doc gets a new ID and URL, so any link already sent goes stale.

The working pipeline:

1. Author the document as **self-contained HTML with embedded CSS** in the
   session scratchpad.
2. Render to PDF with headless Chromium:
   ```
   /opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu \
     --no-sandbox --print-to-pdf=out.pdf --no-pdf-header-footer "file:///abs/path/in.html"
   ```
3. **Verify the PDF** — extract text with `pypdfium2` to confirm key phrases
   landed, and **render pages to PNG and actually look at them**. Page-break
   bugs (orphaned headings, tables split mid-row, half-empty pages) only show
   up visually. Use `break-inside: avoid` on any block that must stay whole.
4. Create the Google Doc from a **Docs-friendly** variant of the same HTML.

**Google Docs strips CSS `columns` and flex layouts.** A multi-column PDF
becomes a long single-column Doc. Tables survive; use a borderless table for
signature blocks instead of flex. Expect the Doc to run longer than the PDF
and say so rather than pretending they match.

### Formatting lessons Ryan has already given

- **Length is a real objection.** A 6-page document reads as "intimidating."
  Fix it with layout — two-column lists, tighter leading, compact type — not
  by cutting content he asked for.
- **"Make it look good" beats "make it short."** When he says copy the
  structure of an existing proposal, mirror that structure section for
  section and let it run as long as it needs to.
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
- **Transition:** Flying V shoots *and releases* the first 3 episodes
  themselves. Straw Hut takes over at episode 4.
- **Payment:** card or ACH on file, charged at the top of each month
- **Studio upgrade** offered at $4,350/mo (Premium)
- **Show title:** TBD, to be developed together
- **Day-to-day contacts:** Robb and his team, names TBD

---

## Document inventory (Google Drive — all private, none shared)

| Document | File ID |
|---|---|
| DWZ — Podcast Services Agreement (current, has final Term language) | `1nGLsgfSD7LHs6k15aEKhN3qEem9nLq0XJM8YC5CVFvE` |
| DWZ — agreement version Ryan actually emailed to Pacaso | `1uKnKSW-XN400kzt2gf8jMgV-siaHxPeAbEQuojszM08` ⚠️ **in Drive trash — see below** |
| DWZ — original proposal (Sep 10, 2026) | `15d24sVuf9zk96bsEakHx71uk1j0OrYVRR1elmnYn500` |
| Flying V Group — proposal | `1iU457UVSsTSjUGIpV-Bj9f3CnOHACSDxTnd36Tq7eCc` |
| DWZ — brainstorm episode template + book outline (Ryan's original) | `1kl5_Rq7fW0HaKr26vwC4RwsKl6gQHGYMtOvkY047kpE` |

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
   Agreement" → Restore. As of the last update this had **not been confirmed
   done.** Ask him.
2. **The sent version is one revision behind.** Doc `1uKnKSW…` (what Pacaso
   has) predates the final Term-language tightening. The current text lives
   in `1nGLsgfSD7LHs6k15aEKhN3qEem9nLq0XJM8YC5CVFvE`. Decide with Ryan
   whether Pacaso needs the update or whether it rides along in redlines.
3. **The "3-60 min break" typo is still unconfirmed.** See above.
4. **Flying V feed hosting is unanswered.** Asked who hosts the RSS and who
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
- The HTML sources for these documents lived in a session scratchpad and are
  **gone** when the session ends. The Google Docs are the surviving source of
  truth; rebuild HTML from them if a PDF is needed again. Consider committing
  future HTML sources into this repo so that stops being true.
- Git: develop on `claude/tourism-podcast-pitch-olu47p`, push with
  `git push -u origin <branch>`. Don't push to `main`.
