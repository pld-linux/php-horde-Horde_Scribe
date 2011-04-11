%define		status		stable
%define		pearname	Horde_Scribe
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Scribe
Name:		php-horde-Horde_Scribe
Version:	1.0.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	b080d317ce4dd12acdfa1eeb2ca67963
URL:		http://pear.horde.org/package/Horde_Scribe/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-pear >= 4:1.3.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Packaged version of the PHP Scribe client.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/examples/Horde/Scribe examples

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Scribe.php
%{php_pear_dir}/Horde/Scribe
%{_examplesdir}/%{name}-%{version}

# ??? external scribe library bundled with Horde_Thrift
%{php_pear_dir}/Horde/Thrift
