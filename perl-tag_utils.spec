%define module  tag_utils
%define name    perl-%{module}
%define version 1.10
%define release %mkrel 10
%define _provides_exceptions XML::Parser::Expat\\|Parse::Yapp::Driver

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl module to convert between various formats for Tree Adjoining Grammars
License:        GPL
Group:          Development/Perl
Url:            http://atoll.inria.fr/packages/packages.html#tag_utils
Source:         ftp://ftp.inria.fr/INRIA/Projects/Atoll/Eric.Clergerie/TAG/%{module}-%{version}.tar.bz2
Obsoletes:      perl-TAG
Provides:       perl-TAG
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl-libxml-perl
Buildarch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
tag_utils is a set of Perl scripts to convert between various formats for Tree
Adjoining Grammars, in particular the XML TAGML format.

%prep
%setup -q -n %{module}-%{version}
chmod 644 TAG/XTAG/Parser.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/TAG*
%{_mandir}/*/*

