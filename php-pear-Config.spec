%include	/usr/lib/rpm/macros.php
%define		_class		Config
%define		_pearname	%{_class}
%define		_status		stable
Summary:	%{_pearname} - class for reading and writing Config-"files"
Summary(pl):	%{_pearname} - klasa do odczytu i zapisu plików konfiguracyjnych
Name:		php-pear-%{_pearname}
Version:	1.10
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	addf5be0d5cd5ec5fa530b18a13dc3d0
URL:		http://pear.php.net/package/Config/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet Config udostêpnia metody do edycji zasobów konfiguracyjnych.
Robi to w sposób zorientowany obiektowo, definiuj±c ka¿dy element
znaleziony w zasobie konfiguracyjnym jako Config_Container ró¿nych
typów (komentarz, sekcja, dyrektywa, odstêp...). Elementy mog± byæ
modyfikowane, dodawane, usuwane, wstawiane. Ten pakiet nie ma s³u¿yæ
tylko do czytania danych konfiguracyjnych, ale tak¿e do edycji ich.
Tylko do czytania danych lepiej u¿ywaæ funkcji typu parse_ini_file(),
które s± du¿o szybsze.

Ta klasa ma w PEAR status: %{_status}.

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
