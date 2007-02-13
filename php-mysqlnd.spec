%define		_rc		alpha
%define		_rel	0.1
Summary:	MySQL native driver for PHP
Summary(pl.UTF-8):	Natywny sterownik MySQL dla PHP
Name:		php-mysqlnd
Version:	5.0.0
Release:	0.%{_rc}.%{_rel}
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	%{name}-%{version}-%{_rc}-20070202.19.tar.bz2
# Source0-md5:	e2e813e79f7496c78117eb451870bc82
URL:		http://dev.mysql.com/downloads/connector/php-mysqlnd/
BuildRequires:	php-devel >= 4:6.0
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
