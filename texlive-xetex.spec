# revision 26330
# category TLCore
# catalog-ctan undef
# catalog-date 2012-05-06 11:41:55 +0200
# catalog-license other-free
# catalog-version 0.9997.5
Name:		texlive-xetex
Epoch:		1
Version:	0.9997.5
Release:	1
Summary:	Unicode and OpenType-enabled TeX engine
Group:		Publishing
URL:		http://tug.org/texlive
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-xetexconfig
Requires:	texlive-xetex.bin

%description
See http://tug.org/xetex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	rm -fr %{_texmfvardir}/web2c/xetex
	%{_sbindir}/texlive.post
    fi

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
mkdir -p %{buildroot}%{_tlpkgdir}
cp -fpar tlpkg/tlpostcode %{buildroot}%{_tlpkgdir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/xetex <<EOF
#
# from xetex:
xetex xetex language.def -etex xetex.ini
xelatex xetex language.dat -etex xelatex.ini
EOF


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:0.9997.5-1
+ Revision: 813185
- Update to latest release.

* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120221-1
+ Revision: 778488
- Rebuild after tlpobj2spec.pl bug correction.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-3
+ Revision: 757832
- Rebuild to reduce used resources

* Tue Nov 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 729095
- texlive-xetex

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719928
- texlive-xetex
- texlive-xetex
- texlive-xetex
- texlive-xetex

