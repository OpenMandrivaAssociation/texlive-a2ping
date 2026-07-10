%global tl_name a2ping
%global tl_revision 52964

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.84p
Release:	%{tl_revision}.1
Summary:	Advanced PS, PDF, EPS converter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/a2ping
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/a2ping.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/a2ping.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(a2ping.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
a2ping is a Perl script command line utility written for Unix that
converts many raster image and vector graphics formats to EPS or PDF and
other page description formats. Accepted input file formats are: PS
(PostScript), EPS, PDF, PNG, JPEG, TIFF, PNM, BMP, GIF, LBM, XPM, PCX,
TGA. Accepted output formats are: EPS, PCL5, PDF, PDF1, PBM, PGM, PPM,
PS, markedEPS, markedPS, PNG, XWD, BMP, TIFF, JPEG, GIF, XPM. a2ping
delegates the low-level work to Ghostscript (GS), pdftops and sam2p.
a2ping fixes many glitches during the EPS to EPS conversion, so its
output is often more compatible and better embeddable than its input.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/a2ping
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support/a2ping
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/a2ping.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/a2ping.man1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/a2ping/HISTORY.txt
%{_datadir}/texmf-dist/texmf-dist/scripts/a2ping/a2ping.pl
