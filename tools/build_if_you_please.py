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
p(7, "A focused, paid audience-growth program for If You Please and the Radio Drama Network YouTube channel — reaching the right listeners for every episode.")
p(8); p(9, 'Program Details')
bullets(['Show: If You Please, Himan Brown’s Radio Mystery Theater (CUNY TV)',
    'Channels grown: the podcast RSS feed and the Radio Drama Network YouTube channel',
    'Program begins: October 1, 2026',
    'Term: six (6) months, October 1, 2026 through March 31, 2027',
    'Scope: promotion and growth only — the show’s team continues to publish all episodes'])
p(14); p(15, "What's Included")
bullets(['Up to four (4) episodes promoted per channel each month: four for the RSS feed and four on YouTube',
    'A dedicated landing page for each promoted episode, driving listens that count toward RSS downloads',
    'Episode-by-episode audience targeting: fans of radio drama, mystery, and old-time radio',
    'A matching YouTube program, promoting episodes to viewers likely to watch and subscribe',
    'Primary focus on native English-speaking countries, plus a worldwide test',
    'Ongoing optimization toward the best-performing episodes, audiences, and countries',
    'A monthly summary of spend and results'])
p(35, 'Investment & Costs')
table(37, [
    ['Cost Component', 'Details'],
    ['Straw Hut Media Fee', '$925 / month. Landing pages, targeting, campaign management, and reporting.'],
    ['Promotion Budget', '$1,075 / month, spent on paid promotion: $650 for the RSS feed and $425 for YouTube.'],
    ['Monthly Total', '$2,000 / month, billed at the start of each month from October 1, 2026.']])
p(39, 'Monthly Total: ', '$2,000 / month', '  ·  billed monthly, six-month term')
p(16, 'This is a starting budget; if results warrant it, the promotion budget can increase by mutual agreement without changing Straw Hut Media’s fee. Promoting more than four episodes per channel in a month would add a modest fee increase, agreed in advance.')
p(27, 'Paid promotion is test-and-learn, and response varies by episode and market. We will manage the budget carefully and report openly, but this proposal does not promise specific download, view, or subscriber numbers.')
p(57, 'Next Steps')
p(58, 'Once signed, we’ll send a short credit card / ACH authorization form and begin setup for an October 1 start.')
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
