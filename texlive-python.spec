# revision 27064
# category Package
# catalog-ctan /macros/latex/contrib/python
# catalog-date 2012-07-03 11:28:15 +0200
# catalog-license gpl
# catalog-version 0.21
Name:		texlive-python
Version:	0.21
Release:	11
Summary:	Embed Python code in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/python
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/python.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/python.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables you to embed Python code in LaTeX, and
insert the script's output in the document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/python/python.sty
%doc %{_texmfdistdir}/doc/latex/python/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.21-1
+ Revision: 813736
- Import texlive-python
- Import texlive-python

