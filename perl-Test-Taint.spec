%define upstream_name    Test-Taint
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Tools to test taintedness
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tie::Array)
BuildRequires: perl(Tie::Hash)
BuildRequires: perl(Tie::Scalar)
BuildRequires: perl(overload)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Tainted data is data that comes from an unsafe source, such as the command
line, or, in the case of web apps, any GET or POST transactions. Read the
the perlsec manpage man page for details on why tainted data is bad, and
how to untaint the data.

When you're writing unit tests for code that deals with tainted data,
you'll want to have a way to provide tainted data for your routines to
handle, and easy ways to check and report on the taintedness of your data,
in standard the Test::More manpage style.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


