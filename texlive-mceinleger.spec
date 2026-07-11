%global tl_name mceinleger
%global tl_revision 79121

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Creating covers for music cassettes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mceinleger
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mceinleger.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mceinleger.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for creating MC-covers on your own. It allows the creation of
simple covers as well as covers with an additional page for more
information about the cassette (table of contents e.g.). The rotating
package is required.

