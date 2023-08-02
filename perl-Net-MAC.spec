#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-MAC
Version  : 2.103622
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/O/OL/OLIVER/Net-MAC-2.103622.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OL/OLIVER/Net-MAC-2.103622.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-mac-perl/libnet-mac-perl_2.103622-2.debian.tar.xz
Summary  : 'Perl extension for representing and manipulating MAC addresses '
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Net-MAC-license = %{version}-%{release}
Requires: perl-Net-MAC-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Net::MAC - Perl extension for representing and manipulating MAC
addresses
VERSION
version 2.103622

%package dev
Summary: dev components for the perl-Net-MAC package.
Group: Development
Provides: perl-Net-MAC-devel = %{version}-%{release}
Requires: perl-Net-MAC = %{version}-%{release}

%description dev
dev components for the perl-Net-MAC package.


%package license
Summary: license components for the perl-Net-MAC package.
Group: Default

%description license
license components for the perl-Net-MAC package.


%package perl
Summary: perl components for the perl-Net-MAC package.
Group: Default
Requires: perl-Net-MAC = %{version}-%{release}

%description perl
perl components for the perl-Net-MAC package.


%prep
%setup -q -n Net-MAC-2.103622
cd %{_builddir}
tar xf %{_sourcedir}/libnet-mac-perl_2.103622-2.debian.tar.xz
cd %{_builddir}/Net-MAC-2.103622
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Net-MAC-2.103622/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-MAC
cp %{_builddir}/Net-MAC-2.103622/LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-MAC/c51ad390b8913daf34257c057bd5f3595d466c2d
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Net-MAC/ffce0bbfc262ff7cefb5881ad710a9bb6bf6dd5f
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::MAC.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-MAC/c51ad390b8913daf34257c057bd5f3595d466c2d
/usr/share/package-licenses/perl-Net-MAC/ffce0bbfc262ff7cefb5881ad710a9bb6bf6dd5f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
