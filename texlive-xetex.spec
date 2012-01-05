# revision 24091
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-xetex
Version:	20111104
Release:	3
Summary:	Unicode and OpenType-enabled TeX engine
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-xetexconfig
Requires:	texlive-xetex.bin
Requires(post):	texlive-tetex

%description
See http://tug.org/xetex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi
    rm -fr %{_texmfvardir}/web2c/xetex/

#-----------------------------------------------------------------------
%files
%{_bindir}/xelatex
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/base/qx-unicode.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/base/qx-unicode.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/base/tex-text.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/base/tex-text.tec
%{_texmfdistdir}/scripts/xetex/perl/lib/PDF/Reuse.pm
%{_texmfdistdir}/scripts/xetex/perl/lib/PDF/Reuse/Util.pm
%{_texmfdistdir}/scripts/xetex/perl/xdv2pdf_mergemarks
%{_tlpkgdir}/tlpostcode/xetex.pl
%_texmf_fmtutil_d/xetex
%doc %{_texmfdistdir}/doc/xetex/base/XeTeX-notes.pdf
%doc %{_texmfdistdir}/doc/xetex/base/XeTeX-notes.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf xetex xelatex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
cp -fpar tlpkg/tlpostcode %{buildroot}%{_tlpkgdir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/xetex <<EOF
xetex xetex language.def -etex xetex.ini
xelatex xetex language.dat -etex xelatex.ini
EOF
