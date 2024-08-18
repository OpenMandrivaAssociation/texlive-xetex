Name:		texlive-xetex
Epoch:		1
Version:	71991
Release:	1
Summary:	Unicode and OpenType-enabled TeX engine
Group:		Publishing
URL:		http://tug.org/texlive
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex.doc.r%{version}.tar.xz
# Stuff in upstream xetex.PLATFORM-OS.tar.xz tarballs comes from the texlive
# package. No need to duplicate it here.
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
%{_texmfdistdir}/fonts/misc/xetex
%{_texmfdistdir}/scripts/texlive-extra/*
%{_tlpkgdir}/tlpostcode/xetex.pl
%_texmf_fmtutil_d/xetex
%doc %{_texmfdistdir}/doc/xetex
%doc %{_texmfdistdir}/doc/man/man1/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

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
