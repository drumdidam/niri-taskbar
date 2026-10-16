%global gittag v0.5.0+niri.26.04
%global debug_package %{nil}

Name:           niri-taskbar
Version:        0.5.0
Release:        1%{?dist}
Summary:        Niri taskbar module for Waybar

License:        MIT
URL:            https://github.com/drumdidam/niri-taskbar
Source0:        %{url}/archive/refs/tags/%{gittag}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust >= 1.87
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       waybar
Requires:       niri >= 26.04

%description
A Waybar CFFI module that shows a taskbar for the Niri compositor.

%prep
%setup -q -c -T
tar -xzf %{SOURCE0} --strip-components=1

%build
cargo build --release --locked

%install
install -Dm0755 target/release/libniri_taskbar.so \
    %{buildroot}%{_libdir}/niri-taskbar/libniri_taskbar.so

%check
cargo test --release --locked

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/niri-taskbar
%{_libdir}/niri-taskbar/libniri_taskbar.so

%changelog
* Fri Oct 16 2026 Sebastian Sernaglia <drumdidam@gmail.com> - 0.5.0-1
- Update niri-ipc to 26.4 for Niri 26.04 support
