%define upstream_name    Test-Taint
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.06
Release:	3

Summary:    Tools to test taintedness
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/Test-Taint-1.06.tar.gz

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




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.40.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 556156
- rebuild for perl 5.12

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 553068
- import perl-Test-Taint


* Wed Jul 14 2010 cpan2dist 1.04-1mdv
- initial mdv release, generated with cpan2dist

