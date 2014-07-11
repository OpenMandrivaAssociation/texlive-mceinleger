# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mceinleger
# catalog-date 2007-01-09 22:36:10 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-mceinleger
Version:	20070109
Release:	8
Summary:	Creating covers for music cassettes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mceinleger
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mceinleger.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mceinleger.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/mceinleger/mceinleger.sty
%doc %{_texmfdistdir}/doc/latex/mceinleger/mceinleger.pdf
%doc %{_texmfdistdir}/doc/latex/mceinleger/mceinleger.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070109-2
+ Revision: 753834
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070109-1
+ Revision: 718981
- texlive-mceinleger
- texlive-mceinleger
- texlive-mceinleger
- texlive-mceinleger

