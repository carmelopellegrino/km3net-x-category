# $Id$
Name:           km3net-x-category
Version:        1.0
Release:        1
Summary:        X menu entry for the KM3NeT group
Group:          KM3NeT
License:        INFN
URL:            https://github.com/carmelopellegrino/km3net-x-category
Source0:        https://github.com/carmelopellegrino/km3net-x-category
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       bash
%description
X menu entry for the KM3NeT group of applications

%define debug_package %{nil}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/xdg/menus/applications-merged/
mkdir -p $RPM_BUILD_ROOT/usr/share/desktop-directories/
mkdir -p $RPM_BUILD_ROOT/usr/share/km3net/icon/

cp km3net.menu $RPM_BUILD_ROOT/etc/xdg/menus/applications-merged/
cp km3net.png $RPM_BUILD_ROOT/usr/share/km3net/icon/
cp km3net.directory $RPM_BUILD_ROOT/usr/share/desktop-directories/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/desktop-directories/km3net.directory
/usr/share/km3net/icon/km3net.png
/etc/xdg/menus/applications-merged/km3net.menu

%changelog
* Thu Nov 19 2015 Carmelo Pellegrino <cpellegrino@km3net.de> 1.0
- First RPM release
