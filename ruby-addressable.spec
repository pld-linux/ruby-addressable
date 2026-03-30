#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	addressable
Summary:	Improved URI/URL Implementation
Name:		ruby-%{pkgname}
Version:	2.8.8
Release:	2
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	51d1a2204c947a6577fb9c0c7a708036
URL:		https://github.com/sporkmonger/addressable
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-launchy >= 0.3.2
BuildRequires:	ruby-rake >= 0.7.3
BuildRequires:	ruby-rspec >= 2.9.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Addressable is a replacement for the URI implementation that is part
of Ruby's standard library. It more closely conforms to the relevant
RFCs and adds support for IRIs and URI templates.

%prep
%setup -q -n %{pkgname}-%{version}
%build
%__gem_helper spec

%if %{with tests}
rspec spec/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE.txt
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
