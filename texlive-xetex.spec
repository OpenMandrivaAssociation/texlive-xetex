%global tl_name xetex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	An extended variant of TeX for use with Unicode sources
Group:		Publishing
URL:		https://www.ctan.org/pkg/xetex
License:	x11
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(babel)
Requires:	texlive(cm)
Requires:	texlive(dvipdfmx)
Requires:	texlive(etex)
Requires:	texlive(firstaid)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(l3backend)
Requires:	texlive(l3kernel)
Requires:	texlive(latex)
Requires:	texlive(latex-fonts)
Requires:	texlive(lm)
Requires:	texlive(plain)
Requires:	texlive(tex-ini-files)
Requires:	texlive(unicode-data)
Requires:	texlive(xetex.bin)
Requires:	texlive(xetexconfig)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
XeTeX is a TeX typesetting engine using Unicode and supporting modern
font technologies such as OpenType, TrueType or Apple Advanced
Typography (AAT), including OpenType mathematics fonts. XeTeX supports
many extensions that reflect its origins in linguistic research; it also
supports micro-typography (as available in pdfTeX). XeTeX was developed
by the SIL (the first version was specifically developed for those
studying linguistics, and using Macintosh computers). XeTeX's immediate
output is an extended variant of DVI format, which is ordinarily
processed by a tightly bound processor (called xdvipdfmx), that produces
PDF. XeTeX is released as part of TeX Live; documentation has arisen
separately. Source code is available from ctan:/systems/texlive/Source/.

