%define name iwlwifi-100-ucode
%define version 39.31.5.1
%define release %mkrel 1

Summary: Intel PRO/Wireless N 100 microcode
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-100-ucode-%{version}.tgz
License: Proprietary
Group: System/Kernel and hardware
Url: http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
The file iwlwifi-100-*.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless N 100 Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.* README.*
/lib/firmware/*.ucode


