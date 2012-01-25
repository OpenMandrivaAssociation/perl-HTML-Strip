%define upstream_name    HTML-Strip
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Perl extension for stripping HTML markup from text
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz


BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module simply strips HTML-like markup from text in a very quick and
brutal manner. It could quite easily be used to strip XML or SGML from text
as well; but removing HTML markup is a much more common problem, hence this
module lives in the HTML:: namespace.

It is written in XS, and thus about five times quicker than using regular
expressions for the same task.

It does _not_ do any syntax checking (if you want that, use the
HTML::Parser manpage), instead it merely applies the following rules:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


