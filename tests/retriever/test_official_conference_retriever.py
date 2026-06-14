from omegaconf import open_dict

from zotero_arxiv_daily.retriever.official_conference_retriever import (
    ACLAnthologyRetriever,
    NeurIPSRetriever,
)


ACL_EVENT_HTML = """
<div class="d-sm-flex align-items-stretch mb-3"><div class="d-block me-2 list-button-row">
<span class="d-inline d-sm-block text-nowrap"><a class="badge text-bg-primary align-middle me-1" href=https://aclanthology.org/2025.acl-long.2.pdf>pdf</a></span></div>
<span class=d-block><strong><a class=align-middle href=/2025.acl-long.2/><span class=acl-fixed-case>G</span>raph<span class=acl-fixed-case>N</span>arrator: Generating Textual Explanations for Graph Neural Networks</a></strong><br>
<a href=/people/bo-pan/>Bo Pan</a> | <a href=/people/liang-zhao/>Liang Zhao</a></span></div>
<div class="card bg-light mb-2 mb-lg-3 collapse abstract-collapse" id=abstract-2025--acl-long--2><div class="card-body p-3 small">Graph representation learning abstract.</div></div>
<div class="d-sm-flex align-items-stretch mb-3"><span class=d-block><strong><a class=align-middle href=/2025.acl-long.3/>Another Paper</a></strong><br>
<a href=/people/a/>A. Author</a></span></div>
</section>
"""


NEURIPS_LIST_HTML = """
<ul class="paper-list">
<li class="conference"><div class="paper-content">
<a title="paper title" href="/paper_files/paper/2025/hash/001-Abstract-Conference.html">Flow Models for Biology</a>
<span class="paper-authors">A. Author, B. Author</span>
</div></li>
</ul>
"""


NEURIPS_DETAIL_HTML = """
<meta name="citation_title" content="Flow Models for Biology">
<meta name="citation_author" content="Author, A.">
<meta name="citation_author" content="Author, B.">
<meta name="citation_pdf_url" content="https://proceedings.neurips.cc/paper_files/paper/2025/file/001-Paper-Conference.pdf">
<meta name="citation_publication_date" content="2026-04-23">
<h1 class="paper-title">Flow Models for Biology</h1>
<p class="paper-abstract"><p>A flow matching model for biological simulation.</p></p>
"""


def test_acl_anthology_retriever_parses_event_page(config):
    with open_dict(config):
        config.source.acl_anthology.events = ["acl"]

    retriever = ACLAnthologyRetriever(config)
    papers = retriever._parse_event_page(ACL_EVENT_HTML, "ACL", 2025)

    assert len(papers) == 2
    assert papers[0].title == "GraphNarrator: Generating Textual Explanations for Graph Neural Networks"
    assert papers[0].authors == ["Bo Pan", "Liang Zhao"]
    assert papers[0].abstract == "Graph representation learning abstract."
    assert papers[0].pdf_url == "https://aclanthology.org/2025.acl-long.2.pdf"
    assert papers[0].publication_date == "2025-01-01"


def test_neurips_retriever_parses_listing_and_detail(config):
    retriever = NeurIPSRetriever(config)

    urls = retriever._parse_listing_page(NEURIPS_LIST_HTML)
    assert urls == [
        "https://proceedings.neurips.cc/paper_files/paper/2025/hash/001-Abstract-Conference.html"
    ]

    paper = retriever._parse_detail_page(NEURIPS_DETAIL_HTML, urls[0], 2025)
    assert paper.title == "Flow Models for Biology"
    assert paper.authors == ["Author, A.", "Author, B."]
    assert paper.abstract == "A flow matching model for biological simulation."
    assert paper.pdf_url.endswith("001-Paper-Conference.pdf")
    assert paper.publication_date == "2026-04-23"
