%include	/usr/lib/rpm/macros.php
%define		_class		Config
%define		_pearname	%{_class}
%define		_status		stable

Summary:	%{_pearname} - class for reading and writing Config-"files"
Summary(pl.UTF-8):	%{_pearname} - klasa do odczytu i zapisu plików konfiguracyjnych
Name:		php-pear-%{_pearname}
Version:	1.10.11
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1a044571bd12d283178511b22dc4fd36
URL:		http://pear.php.net/package/Config/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Suggests:	php-pear-XML_Parser
Suggests:	php-pear-XML_Util
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(XML/Parser.*)' 'pear(XML/Util.*)'

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

%description -l pl.UTF-8
Pakiet Config udostępnia metody do edycji zasobów konfiguracyjnych.
Robi to w sposób zorientowany obiektowo, definiując każdy element
znaleziony w zasobie konfiguracyjnym jako Config_Container różnych
typów (komentarz, sekcja, dyrektywa, odstęp...). Elementy mogą być
modyfikowane, dodawane, usuwane, wstawiane. Ten pakiet nie ma służyć
tylko do czytania danych konfiguracyjnych, ale także do edycji ich.
Tylko do czytania danych lepiej używać funkcji typu parse_ini_file(),
które są dużo szybsze.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
