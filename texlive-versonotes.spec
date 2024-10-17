Name:		texlive-versonotes
Version:	69249
Release:	1
Summary:	Display brief notes on verso pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/versonotes
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/versonotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/versonotes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/versonotes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to place notes on the verso pages of an
otherwise single-sided document. If, in the run of text, you
include a call to the macro \versonote{This is a remark}, then
that text will be placed on the opposite (ie, 'verso') page,
lined up with the macro call.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/versonotes
%{_texmfdistdir}/tex/latex/versonotes
%doc %{_texmfdistdir}/doc/latex/versonotes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
