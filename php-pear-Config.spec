%include	/usr/lib/rpm/macros.php
%define		_class		Config
%define		_pearname	%{_class}
Summary:	%{_pearname} - class for reading and writing Config-"files"
Summary(pl):	%{_pearname} - klasa do odczytu i zapisu plików konfiguracyjnych
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Config package provides methods for editing configuration
datasources. It does so in an object oriented manner, defining each
and every items found in the config datasource as a Config_Container
of various types (comments, sections, directives, blanks, ...). Items
can then be edited, added, removed, inserted. This package is not
intended for reading configuration data only, but for editing them. If
you only want to read your configuration data, use functions like
parse_ini_file() and the like instead, they are much faster.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Container

install %{_pearname}-%{version}/%{_class}.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_class}/Container/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Container

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Container
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Container/*.php
