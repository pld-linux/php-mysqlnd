# TODO
# php_mysqli.h:42:40: ext/mysqli/mysqli_libmysql.h: No such file or directory
%define		_rc		beta
%define		_rel	0.1
Summary:	MySQL native driver for PHP
Summary(pl.UTF-8):	Natywny sterownik MySQL dla PHP
Name:		php-mysqlnd
Version:	5.0.1
Release:	0.%{_rc}.%{_rel}
License:	PHP 3.01
Group:		Development/Languages/PHP
URL:		http://dev.mysql.com/downloads/connector/php-mysqlnd/
Source0:	ftp://mirror2.dataphone.se/pub/mysql/Downloads/Connector-PHP-mysqlnd/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	a23dcb05ce0bc4df229ce08ff6d5a40b
BuildRequires:	php-devel >= 4:5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MySQL native driver for PHP is an additional, alternative way to
connect from PHP 6 to the MySQL Server 4.1 or newer. It is a
replacement for the libmysql, the MySQL Client Library. From now on
you can use ext/mysqli either together with libmysql as you did in the
past or with mysqlnd.

%description -l pl.UTF-8
Natywny sterownik MySQL dla PHP to dodatkowy, alternatywny sposób
łączenia się z PHP 6 do serwera MySQL 4.1 lub nowszego. Jest to
zamiennik libmysql - biblioteki klienckiej MySQL. Od teraz można
używać ext/mysqli wraz z libmysql jak dotychczas, lub z mysqlnd.

%prep
%setup -q -n %{name}-%{version}-%{_rc}
mv php5/ext/mysqli/{config9.m4,config.m4}

%build
cd php5/ext/mysqli
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd php5/ext/mysqli
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
