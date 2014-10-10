%define upstream_name       tag_utils
%define upstream_version    1.12

%if %{_use_internal_dependency_generator}
%define __noautoprov 'perl\\(XML::Parser::Expat\\)|perl\\(Parse::Yapp::Driver\\)'
%else
%define _provides_exceptions XML::Parser::Expat\\|Parse::Yapp::Driver
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Conversion between various formats for Tree Adjoining Grammars
License:	GPL
Group:		Development/Perl
Url:		http://alpage.inria.fr/catalogue.en.html#tag_utils
Source:		https://gforge.inria.fr/frs/download.php/5687/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Generator)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Data::Grove)
BuildRequires:	perl(AppConfig)
BuildRequires:	perl(DBI)
BuildArch:	noarch

%description
tag_utils is a set of Perl scripts to convert between various formats for Tree
Adjoining Grammars, in particular the XML TAGML format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog INSTALL LICENSE README
%{_bindir}/*
%{perl_vendorlib}/TAG*
%{_mandir}/*/*



%changelog
* Fri Jul 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1mdv2010.0
+ Revision: 396697
- new version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.10-11mdv2009.0
+ Revision: 258432
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.10-10mdv2009.0
+ Revision: 246498
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.10-8mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-8mdv2008.0
+ Revision: 86925
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-7mdv2007.0
- Rebuild

* Fri Dec 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-6mdk
- fix name

* Fri Dec 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-5mdk
- spec cleanup
- %%mkrel

* Wed Dec 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.10-4mdk 
- fix buildrequires in a backward compatible way

* Sun Dec 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.10-3mdk 
- fix wrong provides

* Mon Nov 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.10-2mdk 
- fix buildrequires

* Tue Nov 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.10-1mdk 
- first mdk release

