Summary:	Post-processing for scanned and photocopied book pages
Name:		unpaper
Version:	7.0.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://www.flameeyes.com/files/%{name}-%{version}.tar.xz
# Source0-md5:	24be66b049a27b6f841cc7444ceff9cc
URL:		https://www.flameeyes.eu/projects/unpaper
BuildRequires:	ffmpeg-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unpaper is a post-processing tool for scanned sheets of paper,
especially for book pages that have been scanned from previously
created photocopies. The main purpose is to make scanned book pages
better readable on screen after conversion to PDF. Additionally,
unpaper might be useful to enhance the quality of scanned pages before
performing optical character recognition (OCR). unpaper tries to clean
scanned images by removing dark edges that appeared through scanning
or copying on areas outside the actual page content (e.g. dark areas
between the left-hand-side and the right-hand-side of a double- sided
book-page scan). The program also tries to detect disaligned centering
and rotation of pages and will automatically straighten each page by
rotating it to the correct angle. This process is called "deskewing".

%prep
%setup -q

%build
%meson build

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md doc/*.md doc/img
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/unpaper.1*
