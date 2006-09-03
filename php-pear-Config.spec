%include	/usr/lib/rpm/macros.php
%define		_class		Config
%define		_pearname	%{_class}
%define		_status		stable

Summary:	%{_pearname} - class for reading and writing Config-"files"
Summary(pl):	%{_pearname} - klasa do odczytu i zapisu plików konfiguracyjnych
Name:		php-pear-%{_pearname}
Version:	1.10.7
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3a5b343791ceec7fc715cd7f69eefe41
URL:		http://pear.php.net/package/Config/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
