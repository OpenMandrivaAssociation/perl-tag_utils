%define upstream_name       tag_utils
%define upstream_version    1.12

%define module  tag_utils
%define name    perl-%{module}
%define version 1.10
%define release %mkrel 11
%define _provides_exceptions XML::Parser::Expat\\|Parse::Yapp::Driver

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    Conversion between various formats for Tree Adjoining Grammars
License:    GPL
Group:      Development/Perl
Url:        http://alpage.inria.fr/catalogue.en.html#tag_utils
Source:     https://gforge.inria.fr/frs/download.php/5687/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(XML::Generator)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Data::Grove)
BuildRequires:  perl(AppConfig)
Buildarch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
tag_utils is a set of Perl scripts to convert between various formats for Tree
Adjoining Grammars, in particular the XML TAGML format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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
%doc ChangeLog INSTALL LICENSE README
%{_bindir}/*
%{perl_vendorlib}/TAG*
%{_mandir}/*/*

