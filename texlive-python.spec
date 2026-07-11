%global tl_name python
%global tl_revision 60162

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.22
Release:	%{tl_revision}.1
Summary:	Embed Python code in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/python
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/python.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/python.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables you to embed Python code in LaTeX, and insert the
script's output in the document.

