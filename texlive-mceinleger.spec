Name:		texlive-mceinleger
Version:	15878
Release:	2
Summary:	Creating covers for music cassettes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mceinleger
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mceinleger.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mceinleger.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for creating MC-covers on your own. It allows the
creation of simple covers as well as covers with an additional
page for more information about the cassette (table of contents
e.g.). The rotating package is required.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mceinleger
%doc %{_texmfdistdir}/doc/latex/mceinleger

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
