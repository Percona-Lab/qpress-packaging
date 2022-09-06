
%define debug_package %{nil}

Name:		qpress
Version:	11
Release:	2%{?dist}
Summary:	A portable file archiver using QuickLZ
Group:		Applications/File
License:	GPL
URL:		http://www.quicklz.com/
Source0:	http://www.quicklz.com/qpress-11-source.zip
Patch0:		01-include-unistd.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	gcc-c++

%description
qpress is a portable file archiver using QuickLZ and designed to utilize fast
storage systems to their max. It's often faster than file copy because the
destination is smaller than the source. A few features:
· multiple cores, reaching upto 1.1 Gbyte/s in-memory compression
  on a quad core i7
· 64-bit file sizes and tested with terabyte sized archives containing
  millions of files and directories
· pipes and redirection and *nix-like behaviour for scripting and flexibility
· Adler32 checksums to ensure that decompressed data has not been corrupted
· data recovery of damaged archives with 64 Kbyte grannularity
· unbuffered disk I/O (Windows only) to prevent disk cache of other
  applications from being flushed

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1

%build
make %{?_smp_mflags}

%install
test "x$RPM_BUILD_ROOT" != "x/" -a -d "$RPM_BUILD_ROOT" &&
    rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT/usr/bin"
install qpress "$RPM_BUILD_ROOT/usr/bin/"

%files
/usr/bin/qpress

%changelog
* Tue Jul  9 2013 Ignacio Nin <ignacio.nin@percona.com>

- Initial RPM .spec
- Include a patch file for qpress.cpp, which doesn't include unistd.h in the
  source, and uses isatty().
