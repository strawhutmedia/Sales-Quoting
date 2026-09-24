# Flying V proposal built from the DWZ proposal's own .docx export: every
# paragraph/table is a deep copy of a DWZ element, only the text changes.
import copy, docx
from docx.text.paragraph import Paragraph
from docx.table import Table
d = docx.Document('dwz.docx')
body = d.element.body
E = list(body.iterchildren())
sect = E[-1]
out = []

def settext(p, texts):
    runs = p.runs
    for k, r in enumerate(runs):
        r.text = texts[k] if k < len(texts) else ''

def p(i, *texts):
    el = copy.deepcopy(E[i]); settext(Paragraph(el, d), texts); out.append(el)

def bullets(items):
    for it in items: p(17, it)

def table(i, rows, bold_last=False):
    el = copy.deepcopy(E[i]); t = Table(el, d)
    protos = [copy.deepcopy(r._tr) for r in t.rows]
    for r in list(t.rows): el.remove(r._tr)
    for n, row in enumerate(rows):
        tr = copy.deepcopy(protos[0] if n == 0 else (protos[-1] if bold_last and n == len(rows) - 1 else protos[1]))
        el.append(tr)
    t = Table(el, d)
    for r, row in zip(t.rows, rows):
        for c, txt in zip(r.cells, row):
            settext(c.paragraphs[0], [txt])
    out.append(el)


p(0, 'A PODCAST & YOUTUBE GROWTH PARTNERSHIP')
p(1, 'If You Please')
p(2, "Audience Growth for Himan Brown's Radio Mystery Theater — Straw Hut Media")
p(3, 'Prepared for: ', 'StardustBlue / Karen A. Brown')
p(4, 'Prepared by: ', 'Ryan Tillotson, Founder & CEO, Straw Hut Media')
p(5, 'Date: ', 'September 24, 2026')
p(6)
p(7, "A focused, paid audience-growth program for If You Please and the Radio Drama Network YouTube channel — reaching the right listeners for each episode, and turning them into downloads, views, and subscribers.")
p(8); p(9, 'Program Details')
bullets(['Show: If You Please, Himan Brown’s Radio Mystery Theater (CUNY TV)',
    'Channels grown: the podcast RSS feed and the Radio Drama Network YouTube channel',
    'Program begins: October 1, 2026',
    'Term: six (6) months, October 1, 2026 through March 31, 2027',
    'Scope: promotion and audience growth only. Episodes continue to be produced and published by the show’s current team; Straw Hut Media does not publish or manage uploads.'])
p(14); p(15, "What's Included")
p(16, "Each month's work covers both channels:")
bullets(['A dedicated landing page for every episode, built to play the episode and drive listens that count toward the show’s RSS downloads',
    'Episode-by-episode audience research and targeting, reaching listeners of radio drama, mystery, old-time radio, and classic audio storytelling',
    'Paid promotion that sends those audiences to each episode’s landing page',
    'A matching YouTube growth program: promoting episodes to viewers most likely to watch and subscribe to the Radio Drama Network channel',
    'Geographic testing: a primary focus on native English-speaking countries (the U.S., Canada, the U.K., Ireland, Australia, and New Zealand), alongside a worldwide test to find any strong audiences beyond them',
    'Ongoing optimization: shifting budget toward the episodes, audiences, and countries that perform best',
    'A monthly summary of spend and results for both channels'])
p(35, 'Investment & Costs')
p(36, 'The program runs on a single monthly amount, split between Straw Hut Media’s fee and the promotion budget itself.')
table(37, [
    ['Cost Component', 'Details'],
    ['Straw Hut Media Fee', '$925 / month. Covers landing pages, audience research and targeting, campaign management and optimization, and monthly reporting.'],
    ['Promotion Budget', '$1,075 / month, spent on paid promotion for the show across the RSS and YouTube programs.'],
    ['Monthly Total', '$2,000 / month, billed at the start of each month from October 1, 2026.']])
p(39, 'Monthly Total: ', '$2,000 / month', '  ·  billed monthly, six-month term')
p(16, 'This is a starting budget. If the results warrant it, we can increase the promotion budget at any point by mutual agreement.')
p(27, 'Paid promotion is an ongoing test-and-learn process, and audience response varies by episode, platform, and market. Straw Hut Media will manage the budget carefully and report openly on what it delivers, but this proposal does not promise any specific number of downloads, views, or subscribers.')
p(57, 'Next Steps')
p(58, 'Once this proposal is signed, we’ll send a short authorization form to keep a credit card or bank account (ACH) on file for the monthly charge, and begin setup so the program is live on October 1.')
p(59, 'Acceptance')
p(60, 'By signing below, both parties agree to move forward on the terms outlined in this proposal.')
p(61)
for i, t in zip(range(62, 67), ['Straw Hut Media', 'By: ______________________________________', 'Name: Ryan Tillotson', 'Title: Founder & CEO', 'Date: __________________']): p(i, t)
p(67)
for i, t in zip(range(69, 74), ['StardustBlue', 'By: ______________________________________', 'Name: Karen A. Brown', 'Title: __________________', 'Date: __________________']): p(i, t)
p(75, 'Ryan Tillotson')
p(76, 'Founder & CEO, Straw Hut Media')
p(77, 'ryan@strawhutmedia.com  ·  760.807.7138  ·  7201 Melrose Ave., Suite 203, Los Angeles, CA 90046')

for el in E[:-1]: body.remove(el)
for el in out: body.insert(len(body) - 1, el)
for fp in d.sections[0].footer.paragraphs:
    for r in fp.runs:
        if 'DIE WITH ZERO' in r.text: r.text = r.text.replace('DIE WITH ZERO PODCAST', 'IF YOU PLEASE')
d.core_properties.title = 'If You Please Growth Proposal'
d.save('karen.docx')
t = '\n'.join(x.text for x in docx.Document('fv.docx').paragraphs)
print('saved', 'Die With Zero' in t, 'Dillon' in t, [f.text for f in docx.Document('fv.docx').sections[0].footer.paragraphs])
